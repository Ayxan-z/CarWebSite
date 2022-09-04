from rest_framework.permissions import BasePermission


class IsOwnerOrSuperUser(BasePermission):
    message = 'You must be the owner of this post.'
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_superuser


class IsOwnerOrSuperUserImage(BasePermission):
    message = 'You must be the owner of this image.'
    def has_object_permission(self, request, view, obj):
        return obj.post.user == request.user or request.user.is_superuser
