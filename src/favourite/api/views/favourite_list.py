from rest_framework.views import APIView
from favourite.api.serializers import FavouriteListSerializer
from favourite.models import FavouriteModel
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated


class FavouriteListView(APIView, PageNumberPagination):
    permission_classes = (IsAuthenticated,)
    page_size = 5

    def get(self, request):
        results = self.paginate_queryset(FavouriteModel.objects.filter(user=request.user), request, view=self)
        posts = [i['post'] for i in FavouriteListSerializer(results, many=True, context={'request': request}).data]
        return self.get_paginated_response(posts)