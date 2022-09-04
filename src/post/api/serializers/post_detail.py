from rest_framework import serializers
from post.models import PostModel
from datetime import datetime


class PostDetailSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField(method_name='get_post_images', source='post_images')
    class Meta:
        model = PostModel
        exclude = ('id',)

    def get_post_images(self, obj):
        return [self.context['request'].build_absolute_uri(i.image.url) for i in obj.post_images.all()]

    is_favourite = serializers.SerializerMethodField(method_name='get_is_favourite')
    def get_is_favourite(self, obj):
        user = self.context['request'].user
        return user.favourites.filter(post=obj.id).exists() if user.id else False

    is_owner = serializers.SerializerMethodField(method_name='get_is_owner')
    get_is_owner = lambda self, obj: self.context['request'].user.id == obj.user.id

    phone_number = serializers.SerializerMethodField(method_name='get_phone_number')
    def get_phone_number(self, obj):
        number = str(obj.phone_number.national_number)
        return f"(0{number[:2]}) {number[2:5]}-{number[5:7]}-{number[7:]}"

    extra_boolean_fields = serializers.SerializerMethodField(method_name='get_extra_boolean_fields')
    get_extra_boolean_fields = lambda self, obj: [i.name for i in obj.extra_boolean_fields.all()]

    user = serializers.SerializerMethodField(method_name='get_user_name')
    get_user_name = lambda self, obj: obj.user.name

    brand = serializers.SerializerMethodField(method_name='get_brand_name')
    get_brand_name = lambda self, obj: obj.brand.name if obj.brand else None

    auto_model = serializers.SerializerMethodField(method_name='get_auto_model_name')
    get_auto_model_name = lambda self, obj: obj.auto_model.name if obj.auto_model else None

    category = serializers.SerializerMethodField(method_name='get_category_name')
    get_category_name = lambda self, obj: obj.category.name if obj.category else None
    
    mileage_type = serializers.SerializerMethodField(method_name='get_mileage_type_name')
    get_mileage_type_name = lambda self, obj: obj.mileage_type.name if obj.mileage_type else None

    color = serializers.SerializerMethodField(method_name='get_color_name')
    get_color_name = lambda self, obj: obj.color.name if obj.color else None

    price_type = serializers.SerializerMethodField(method_name='get_price_type_name')
    get_price_type_name = lambda self, obj: obj.price_type.name if obj.price_type else None

    prior_owners_count = serializers.SerializerMethodField(method_name='get_prior_owners_count_name')
    get_prior_owners_count_name = lambda self, obj: obj.prior_owners_count.name if obj.prior_owners_count else None

    seats_count = serializers.SerializerMethodField(method_name='get_seats_count_count')
    get_seats_count_count = lambda self, obj: obj.seats_count.count if obj.seats_count else None

    fuel_type = serializers.SerializerMethodField(method_name='get_fuel_type_name')
    get_fuel_type_name = lambda self, obj: obj.fuel_type.name if obj.fuel_type else None

    gear = serializers.SerializerMethodField(method_name='get_gear_name')
    get_gear_name = lambda self, obj: obj.gear.name if obj.gear else None

    transmission = serializers.SerializerMethodField(method_name='get_transmission_name')
    get_transmission_name = lambda self, obj: obj.transmission.name if obj.transmission else None

    year = serializers.SerializerMethodField(method_name='get_year_year')
    get_year_year = lambda self, obj: obj.year.year if obj.year else None

    engine_volume = serializers.SerializerMethodField(method_name='get_engine_volume_name')
    get_engine_volume_name = lambda self, obj: obj.engine_volume.volume if obj.engine_volume else None

    market = serializers.SerializerMethodField(method_name='get_market_name')
    get_market_name = lambda self, obj: obj.market.name if obj.market else None

    city = serializers.SerializerMethodField(method_name='get_city_name')
    get_city_name = lambda self, obj: obj.city.name if obj.city else None

    creation_date = serializers.SerializerMethodField(method_name='get_creation_date')
    def get_creation_date(self, obj):
        hour = obj.creation_date.hour + 4
        return f"{datetime.strftime(obj.creation_date, '%d.%m.%Y')} {hour if hour < 24 else hour-24}:{obj.creation_date.minute}"