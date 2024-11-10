from django.urls import path
from . import views

urlpatterns = [
    # URL for function-based view (listing all books)
    path('books/', views.list_books, name='list_books'),
    
    # URL for class-based view (library details)
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
