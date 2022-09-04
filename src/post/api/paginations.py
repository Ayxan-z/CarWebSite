from rest_framework.pagination import PageNumberPagination


class AllPostListPagination(PageNumberPagination):
    page_size = 20