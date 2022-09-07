from post.models import PostModel
from post.api.serializers import PostDetailSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class PostDetailView(APIView):
    def get(self, request, *args, **kwargs):
        obj = PostModel.objects.filter(id=self.kwargs['pk'])
        if obj.exists():
            try:
                obj.update(views=obj[0].views+1)
            except: pass

        return Response(
            PostDetailSerializer(obj, many=True, context={'request': request}).data
        )