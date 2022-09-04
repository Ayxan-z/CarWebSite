from rest_framework import serializers
from choices.models import ExtraBooleanFieldsModel
from django.db import IntegrityError
from post.models import (PostModel,
                        PostImageModel)


class PostImageUpdateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImageModel
        exclude = ('post',)

class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImageModel
        exclude = ('post',)

class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraBooleanFieldsModel
        fields = '__all__'

class PostUpdateDeleteSerializer(serializers.ModelSerializer):
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
        exclude = ('creation_date', 'views')
        r = {'required': True, 'allow_null': False}
        extra_kwargs = {'brand': r, 'auto_model': r, 'category': r, 'mileage_type': r, 
                        'color': r, 'price_type': r, 'engine_power': r, 'fuel_type': r,
                        'gear': r, 'transmission': r, 'engine_volume': r, 'city': r,
                        'mileage': r, 'price': r, 'year': r}

    def validate(self, attrs):
        try: post_brand = attrs['brand']
        except: post_brand = PostModel.objects.get(id=int(self.context['view'].kwargs['pk'])).brand

        try: auto_model = attrs['auto_model']
        except: auto_model = PostModel.objects.get(id=int(self.context['view'].kwargs['pk'])).auto_model

        if auto_model.brand.id != post_brand.id:
            raise serializers.ValidationError(f"This brand '{post_brand.name}' does not have such a model, '{auto_model.name}'")

        return attrs

    def update(self, instance, validated_data):
        images = validated_data.pop('uploaded_images', None)
        extra_fields = validated_data.pop('extra_fields', [])

        try: instance.extra_boolean_fields.set(extra_fields)
        except IntegrityError:
            raise serializers.ValidationError("These extra fields are not exist.")

        if images:
            if len(instance.post_images.all()) + len(images) > 15:
                raise serializers.ValidationError("Up to 15 images can be sent")
            post_image_model_instance = [PostImageModel(post=instance, image=image) for image in images]
            PostImageModel.objects.bulk_create(
                post_image_model_instance
            )
        return super().update(instance, validated_data)