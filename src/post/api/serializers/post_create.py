from rest_framework import serializers
from choices.models import ExtraBooleanFieldsModel
from django.db import IntegrityError
from post.models import (PostModel,
                        PostImageModel)


class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImageModel
        fields = '__all__'

class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraBooleanFieldsModel
        fields = '__all__'

class PostCreateSerializer(serializers.ModelSerializer):
    extra_boolean_fields = ExtraSerializer(many=True, read_only=True)
    extra_fields = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        write_only=True,
        default=[],
        allow_empty=True
    )

    images = PostImagesSerializer(many=True, read_only=True, source='post_images')
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=500, allow_empty_file=False, use_url=True),
        write_only=True
    )

    class Meta:
        model = PostModel
        exclude = ('creation_date', 'views', 'user')
        r = {'required': True, 'allow_null': False}
        extra_kwargs = {'brand': r, 'auto_model': r, 'category': r, 'mileage_type': r, 
                        'color': r, 'price_type': r, 'engine_power': r, 'fuel_type': r,
                        'gear': r, 'transmission': r, 'engine_volume': r, 'city': r,
                        'mileage': r, 'price': r, 'year': r}

    def validate(self, attrs):
        auto_model = attrs['auto_model']
        if auto_model.brand.id != attrs['brand'].id:
            raise serializers.ValidationError(f"This brand '{attrs['brand'].name}' does not have such a model, '{auto_model.name}'")

        return attrs

    def create(self, validated_data):
        uploaded_data = validated_data.pop('uploaded_images')
        extra_fields_data = validated_data.pop('extra_fields')

        if len(uploaded_data) > 15:
            raise serializers.ValidationError("Up to 15 images can be sent")

        if len(uploaded_data) < 3:
            raise serializers.ValidationError("At least 3 images can be sent")

        new_product = PostModel.objects.create(**validated_data)
        try:
            new_product.extra_boolean_fields.set(extra_fields_data)
        except IntegrityError:
            new_product.delete()
            raise serializers.ValidationError("These extra fields are not exist.")

        for uploaded_item in uploaded_data:
            new_product_image = PostImageModel.objects.create(post=new_product, image=uploaded_item)
        return new_product