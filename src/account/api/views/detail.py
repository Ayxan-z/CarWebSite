from rest_framework.permissions import IsAuthenticated
from account.api.serializers import AccountDetailSerializer
from rest_framework.generics import RetrieveUpdateAPIView
from account.models import User
from django.shortcuts import get_object_or_404


class AccountDetailView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = AccountDetailSerializer
    http_method_names = ('get', 'put', 'head', 'options')

    def get_object(self):
        queryset = self.get_queryset()
        return get_object_or_404(queryset, id=self.request.user.id)