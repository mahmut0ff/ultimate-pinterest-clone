from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Board
from apps.users.serializers import UserSerializer

User = get_user_model()


class BoardCreateSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Board
        fields = ["id", "title", "description", "owner", "created_at"]