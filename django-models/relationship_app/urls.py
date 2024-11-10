from django.urls import path
from . import views
from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    # URL for function-based view (listing all books)
    path('books/', views.list_books, name='list_books'),
    
    # URL for class-based view (library details)
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
urlpatterns = [
    # URL for user login
    path('login/', views.login_view, name='login'),
    
    # URL for user registration
    path('register/', views.register, name='register'),
    
    # URL for user logout
    path('logout/', views.logout_view, name='logout'),
    
    # Add other URL patterns here, such as for books, libraries, etc.
    path("LogoutView.as_view(template_name=", "LoginView.as_view(template_name="),

]