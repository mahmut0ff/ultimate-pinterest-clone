from django.contrib import admin
from .models import Pin, Comment, Like, Follow


@admin.register(Pin)
class PinAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "owner", "board", "created_at")
    search_fields = ("title", "description")
    list_filter = ("created_at", "board")
    raw_id_fields = ("owner", "board")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "pin", "created_at")
    search_fields = ("text",)
    list_filter = ("created_at",)
    raw_id_fields = ("user", "pin")


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "pin", "created_at")
    list_filter = ("created_at",)
    raw_id_fields = ("user", "pin")


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ("id", "follower", "following", "created_at")
    list_filter = ("created_at",)
    raw_id_fields = ("follower", "following")