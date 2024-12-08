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
    path('post/<int:post_id>/comment/new/', add_comment, name='comment-add'),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    ["post/<int:pk>/delete/", "post/<int:pk>/update/", "post/new/"]

]
 ["comment/<int:pk>/update/", "post/<int:pk>/comments/new/"]
["tags/<slug:tag_slug>/", "PostByTagListView.as_view()"]
