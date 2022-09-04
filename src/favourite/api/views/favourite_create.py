from rest_framework.generics import CreateAPIView
from favourite.api.serializers import FavouriteCreateSerializer
from favourite.models import FavouriteModel
from rest_framework.permissions import IsAuthenticated


class FavouriteCreateView(CreateAPIView):
    serializer_class = FavouriteCreateSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return FavouriteModel.objects.filter(user=self.request.user)