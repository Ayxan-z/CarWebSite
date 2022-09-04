from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from account.api.views import (CreateUserView,
                            UpdatePassword,
                            EmailTokenObtainPairView,
                            MyPostsView,
                            AccountDetailView,
                            AccountDeleteView)


app_name = 'account'
urlpatterns = [
    path('token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('change-password/', UpdatePassword.as_view(), name='change-password'),
    path('my-posts/', MyPostsView.as_view(), name='my-posts'),
    path('detail/', AccountDetailView.as_view(), name='detail'),
    path('delete/', AccountDeleteView.as_view(), name='delete'),
]