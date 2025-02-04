from rest_framework.permissions import BasePermission

class IsReviewOwner(BasePermission):
    """
    Custom permission to only allow the owner of a review to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
