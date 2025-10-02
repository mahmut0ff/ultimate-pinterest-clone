from django.db import models
from apps.boards.models import Board
from django.contrib.auth import get_user_model

User = get_user_model()


class Pin(models.Model):
    board = models.ForeignKey(
        Board,
        on_delete=models.CASCADE,
        related_name="pins"
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="pins"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="pins/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    pin = models.ForeignKey(
        Pin,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.pin}"


class Like(models.Model):
    pin = models.ForeignKey(
        Pin,
        on_delete=models.CASCADE,
        related_name="likes"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="likes"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("pin", "user")  # One like per user

    def __str__(self):
        return f"{self.user} liked {self.pin}"


class Follow(models.Model):
    follower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following"
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="followers"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("follower", "following")  # One follow per pair

    def __str__(self):
        return f"{self.follower} follows {self.following}"