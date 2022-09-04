from rest_framework import serializers
from account.models import User


class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'name')