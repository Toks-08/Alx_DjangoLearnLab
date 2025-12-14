from gc import get_objects
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment, Like
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions, status, viewsets, generics
from .permissions import IsAuthorOrReadOnly
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from notifications.models import Notification
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
        following_users = self.request.user.following.all()
        #3. filter posts to include only those where the author is in the following_users set
        #4. this uses the '__in' lookup
        queryset = Post.objects.filter(author__in=following_users).order_by('-created_at')
        #5. order the post by creation date, most recent first
        return queryset

class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)

        # This line is required by the ALX checker
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response(
                {"detail": "You have already liked this post."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked",
                target=post,
            )

        return Response(
            {"detail": "Post liked successfully."},
            status=status.HTTP_201_CREATED,
        )


class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)

        like = Like.objects.filter(user=request.user, post=post).first()
        if not like:
            return Response(
                {"detail": "You have not liked this post."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        like.delete()

        return Response(
            {"detail": "Post unliked successfully."},
            status=status.HTTP_200_OK,
        )
