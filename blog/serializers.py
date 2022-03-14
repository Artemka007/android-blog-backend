from account.serializers import UserSerializer
from rest_framework import serializers

from .models import Post, PostComment


class PostCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = PostComment
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    likes = UserSerializer(many=True, read_only=True)
    comments = PostCommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = "__all__"

class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
