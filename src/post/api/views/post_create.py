from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from post.api.serializers import PostCreateSerializer
from post.models import PostModel


class PostCreateView(CreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)