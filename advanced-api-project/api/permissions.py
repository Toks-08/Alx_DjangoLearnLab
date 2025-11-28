from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # SAFE METHODS: GET, HEAD, OPTIONS → always allowed
        if request.method in permissions.SAFE_METHODS:
            return True

        # Otherwise, user must be the owner of the book
        return obj.created_by == request.user
