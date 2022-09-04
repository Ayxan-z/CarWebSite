from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from account.api.serializers import MyPostsSerializer
from account.models import User
from account.api.paginations import MyPostPagination


class MyPostsView(ListAPIView):
    serializer_class = MyPostsSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = MyPostPagination

    def get_queryset(self):
        return User.objects.get(id=self.request.user.id).posts.all().order_by('-id')