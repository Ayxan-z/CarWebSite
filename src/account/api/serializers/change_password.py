from rest_framework.serializers import Serializer, CharField
from django.contrib.auth.password_validation import validate_password


class ChangePasswordSerializer(Serializer):
    old_password = CharField(required=True)
    new_password = CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value