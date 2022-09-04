from rest_framework import serializers
from favourite.models import FavouriteModel


class FavouriteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteModel
        fields = ('post',)

    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        queryset = FavouriteModel.objects.filter(post=attrs['post'], user=attrs['user'])
        if queryset.exists():
            raise serializers.ValidationError('Already have')
        return attrs