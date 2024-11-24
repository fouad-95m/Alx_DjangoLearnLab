from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList

# Initialize the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# Define URL patterns
urlpatterns = [
    # Existing ListAPIView endpoint
    path('books/', BookList.as_view(), name='book-list'),

    # Include router-generated URLs
    path('', include(router.urls)),
]
