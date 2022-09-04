from account.api.permissions import NotAuthenticated
from account.api.throttles import RegisterThrottle
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from account.api.serializers import RegisterSerializer


class CreateUserView(CreateAPIView):
    throttle_classes = [RegisterThrottle]
    model = get_user_model()
    serializer_class = RegisterSerializer
    permission_classes = [NotAuthenticated]