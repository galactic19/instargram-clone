from django.contrib import admin
from .models import Tag, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['photo','caption', 'author', 'created_at', ]
    verbose_name = '포스트 관리'