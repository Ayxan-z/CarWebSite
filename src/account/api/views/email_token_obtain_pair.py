from rest_framework_simplejwt.views import TokenObtainPairView
from account.api.serializers import TokenObtainPairSerializer


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer