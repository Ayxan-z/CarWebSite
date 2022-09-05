from rest_framework.serializers import ModelSerializer
from account.models import User


class AccountDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email')
        extra_kwargs = {'name': {'required': 0}, 'email': {'required': 0}}