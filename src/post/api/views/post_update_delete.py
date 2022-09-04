from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.mixins import DestroyModelMixin
from post.models import PostModel, PostImageModel
from post.api.serializers import PostUpdateDeleteSerializer, PostImageUpdateDeleteSerializer
from post.api.permissions import IsOwnerOrSuperUser, IsOwnerOrSuperUserImage
from rest_framework.response import Response
from rest_framework import status


class PostUpdateDeleteView(RetrieveUpdateAPIView, DestroyModelMixin):
    queryset = PostModel.objects.all()
    serializer_class = PostUpdateDeleteSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwnerOrSuperUser]
    http_method_names = ['get', 'patch', 'delete', 'head', 'options']

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class PostImageUpdateDeleteView(RetrieveUpdateAPIView, DestroyModelMixin):
    queryset = PostImageModel.objects.all()
    serializer_class = PostImageUpdateDeleteSerializer
    lookup_field = 'pk'
    permission_classes = [IsOwnerOrSuperUserImage]
    http_method_names = ['put', 'delete', 'head', 'options']

    def delete(self, request, *args, **kwargs):
        if len(PostImageModel.objects.get(id=kwargs['pk']).post.post_images.all()) > 3:
            return self.destroy(request, *args, **kwargs)
        return Response('At least 3 images can be sent', status=status.HTTP_400_BAD_REQUEST)