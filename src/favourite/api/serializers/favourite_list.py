from rest_framework import serializers
from favourite.models import FavouriteModel
from account.api.serializers import MyPostsSerializer


class FavouriteListSerializer(serializers.ModelSerializer):
    post = MyPostsSerializer()

    class Meta:
        model = FavouriteModel
        fields = ('post',)