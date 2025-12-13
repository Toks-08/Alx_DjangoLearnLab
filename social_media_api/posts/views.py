from django.shortcuts import render
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from rest_framework.generics import ListAPIView
# Create your views here
class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        post_pk = self.kwargs.get('post_pk')
        return Comment.objects.filter(post_id=post_pk)

    def perform_create(self, serializer):
        # Retrieve the post instance using the post_pk from the URL
        post_instance = Post.objects.get(pk=self.kwargs.get('post_pk'))

        # Save the comment, explicitly setting the FK fields
        serializer.save(
            post=post_instance,
            author=self.request.user
        )

class FeedListView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        #1. get the list of users the current user is following
        #2. request.following.all()returns a queryset of user objects
        following_user = self.request.user.following.all()
        #3. filter posts to include only those where the author is in the following_users set
        #4. this uses the '__in' lookup
        queryset = Post.objects.filter(author__in=following_user).order_by('-created_at')
        #5. order the post by creation date, most recent first
        return queryset



