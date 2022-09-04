from rest_framework.views import APIView
from account.api.serializers import AccountDetailSerializer
from rest_framework.permissions import IsAuthenticated
from account.models import User
from rest_framework.response import Response


class AccountDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(AccountDetailSerializer(User.objects.filter(id=request.user.id), many=True).data)