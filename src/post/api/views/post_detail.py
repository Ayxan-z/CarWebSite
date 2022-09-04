from rest_framework.generics import RetrieveAPIView
from post.models import PostModel
from post.api.serializers import PostDetailSerializer


class PostDetailView(RetrieveAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        obj = PostModel.objects.filter(id=kwargs['pk'])
        if obj.exists():
            try:
                obj.update(views=obj[0].views+1)
            except: pass
        return super().get(request, *args, **kwargs)