from django.db import models
from django.urls import reverse
from django.conf import settings


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = '태그 관리'

    def __str__(self):
        return self.name
    

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='', help_text='파일첨부는 필수 항목 입니다.')
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag_set = models.ManyToManyField(Tag, blank=True)
    location = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = '포스트 관리'

    def __str__(self):
        return self.caption
    
    def get_absolute_url(self):
        return reverse("instargram:post_detail", args=[self.pk])
    
    