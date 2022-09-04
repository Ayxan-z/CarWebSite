from django.urls import path
from .views import (PostCreateView,
                    ChoicesAutoModelsView,
                    ChoicesListView,
                    PostUpdateDeleteView,
                    PostImageUpdateDeleteView,
                    PostDetailView,
                    PostListView)


app_name = 'post'
urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('choices/', ChoicesListView.as_view(), name='choices'),
    path('models-choices/', ChoicesAutoModelsView.as_view(), name='models-choices'),
    path('update-delete/<pk>', PostUpdateDeleteView.as_view(), name='post-update-delete'),
    path('image-update-delete/<pk>', PostImageUpdateDeleteView.as_view(), name='post-image-update-delete'),
    path('detail/<pk>', PostDetailView.as_view(), name='post-detail'),
    path('list/', PostListView.as_view(), name='post-list'),
]