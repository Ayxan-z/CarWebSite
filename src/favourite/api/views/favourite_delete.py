from rest_framework.views import APIView
from favourite.models import FavouriteModel
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


class FavouriteDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        obj = FavouriteModel.objects.filter(post=kwargs['pk'], user=self.request.user)
        if obj.exists():
            obj.delete()
            return Response('No Content', status=status.HTTP_204_NO_CONTENT)
        return Response('Not Found', status=status.HTTP_404_NOT_FOUND)