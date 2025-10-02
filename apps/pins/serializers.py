from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Pin, Comment, Like, Follow
from apps.boards.models import Board

from apps.users.serializers import UserSerializer

User = get_user_model()

class PinSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    board = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all())

    class Meta:
        model = Pin
        fields = ["id", "title", "description", "image", "owner", "board", "created_at"]


class PinCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField() 
    class Meta:
        model = Pin

        fields = ["title", "description", "image", "owner", "board"]


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    pin = serializers.PrimaryKeyRelatedField(queryset=Pin.objects.all())

    class Meta:
        model = Comment
        fields = ["id", "text", "user", "pin", "created_at"]


class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    pin = serializers.PrimaryKeyRelatedField(queryset=Pin.objects.all())

    class Meta:
        model = Like
        fields = ["id", "user", "pin", "created_at"]


class FollowSerializer(serializers.ModelSerializer):
    follower = UserSerializer(read_only=True)
    following = UserSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ["id", "follower", "following", "created_at"]