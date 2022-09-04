from django.contrib.auth import update_session_auth_hash
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from account.api.serializers import ChangePasswordSerializer


class UpdatePassword(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):  # sourcery skip: extract-method
        self.object = self.request.user
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.data.get('old_password')
            if not self.object.check_password(old_password):
                return Response({'old_password': 'wrong_password'}, status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            update_session_auth_hash(request, self.object)
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)