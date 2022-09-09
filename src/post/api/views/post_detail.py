from post.models import PostModel
from post.api.serializers import PostDetailSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from post.api.throttles import DetailViewThrottle


class PostViewView(APIView):
    throttle_classes = (DetailViewThrottle,)

    def get(self, request, *args, **kwargs):
        try:
            kwargs['obj'].update(views=kwargs['obj'][0].views + 1)
            return Response(1)
        except: Response(0)


class PostDetailView(APIView):
    def get(self, request, *args, **kwargs):
        obj = PostModel.objects.filter(id=self.kwargs['pk'])
        if obj.exists():
            kwargs['obj'] = obj
            view = PostViewView.as_view()
            view(request=self.request._request, *args, **kwargs)

        return Response(
            PostDetailSerializer(obj, many=True, context={'request': request}).data
        )