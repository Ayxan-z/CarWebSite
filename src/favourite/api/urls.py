from django.urls import path
from favourite.api.views import (FavouriteListView,
                                FavouriteCreateView,
                                FavouriteDeleteView)


app_name = 'favourite'
urlpatterns = [
    path('list/', FavouriteListView.as_view(), name='favourite-list'),
    path('create/', FavouriteCreateView.as_view(), name='favourite-create'),
    path('delete/<pk>', FavouriteDeleteView.as_view(), name='favourite-delete'),
]