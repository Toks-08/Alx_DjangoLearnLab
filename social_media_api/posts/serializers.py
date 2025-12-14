from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(
        source='author.username',
        read_only=True,
        help_text="The username of the post's creator. Automatically set by the system."
    )

    comments = serializers.StringRelatedField(
        many=True,
        read_only=True,
        help_text="List of comments related to this post (represented as strings defined in the Comment model's __str__).",
    )

    class Meta:
        model = Post
        fields = ['id','title','content','author','author_username','created_at','updated_at','comments']

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(
        source='author.username',
        read_only=True,
        help_text="The username of the comment's author. Automatically set by the system."
    )

    class Meta:
        model = Comment
        fields = ['id','post','content','author','author_username','created_at','updated_at']