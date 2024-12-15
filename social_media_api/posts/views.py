from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import Post
from rest_framework import status, permissions
from .models import Like, Post
from django.shortcuts import get_object_or_404
from notifications.models import Notification

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        feed = [{"id": post.id, "author": post.author.username, "title": post.title, "content": post.content, "created_at": post.created_at} for post in posts]
        return Response(feed)



class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({"error": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        like = Like.objects.create(user=request.user, post=post)

        # Create notification
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )

        return Response({"message": "Post liked successfully."}, status=status.HTTP_201_CREATED)

class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        like = Like.objects.filter(user=request.user, post=post).first()
        if not like:
            return Response({"error": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        like.delete()
        return Response({"message": "Post unliked successfully."}, status=status.HTTP_200_OK)

["generics.get_object_or_404(Post, pk=pk)", "Like.objects.get_or_create(user=request.user, post=post)"]
