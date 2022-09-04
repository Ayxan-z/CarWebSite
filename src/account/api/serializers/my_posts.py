from post.models import PostModel
from post.api.serializers import PostDetailSerializer
from rest_framework import serializers


class MyPostsSerializer(PostDetailSerializer):
    image = serializers.SerializerMethodField(method_name='get_post_images', source='post_images')

    class Meta:
        model = PostModel
        fields = ('id', 'is_favourite', 'image', 'price', 'price_type', 'brand', 'auto_model', 'year', 'engine_volume', 'mileage', 'city', 'creation_date')

    def get_post_images(self, obj):
        return self.context['request'].build_absolute_uri(obj.post_images.first().image.url)