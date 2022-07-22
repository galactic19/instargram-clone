from django.contrib import admin
from .models import Tag, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk','photo','caption', 'author', 'created_at', ]
    list_display_links = ['pk', 'caption']
    verbose_name = '포스트 관리'
    

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    verbose_name = '태그 관리'
