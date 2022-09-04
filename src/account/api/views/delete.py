from rest_framework.views import APIView
from account.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


class AccountDeleteView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        obj = User.objects.filter(id=request.user.id)
        if obj.exists():
            obj.delete()
            return Response('No Content', status=status.HTTP_204_NO_CONTENT)
        return Response('Not Found', status=status.HTTP_404_NOT_FOUND)