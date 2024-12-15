from rest_framework import permissions

class IsAuthorPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

# posts/urls.py
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = router.urls