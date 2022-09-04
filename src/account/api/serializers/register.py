from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from account.models import User


class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = get_user_model()
        fields = ['name', 'email', 'password']

    def validate(self, attr):
        validate_password(attr['password'])
        return attr

    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data['email'],
            name = validated_data['name'],
            # username = validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user