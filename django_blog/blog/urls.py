from django.contrib.auth import views as auth_views
from django.urls import path
from . import views  # For custom views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', name='post-list'),
    path('post/<int:pk>/',name='post-detail'),
    path('post/new/', name='post-create'),
    path('post/<int:pk>/edit/' ,name='post-update'),
    path('post/<int:pk>/delete/', name='post-delete'),
    ["post/<int:pk>/delete/", "post/<int:pk>/update/", "post/new/"]
]
