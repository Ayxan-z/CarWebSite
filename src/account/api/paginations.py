from rest_framework.pagination import PageNumberPagination


class MyPostPagination(PageNumberPagination):
    page_size = 5