import re

from django.db import models
from django.contrib.auth import get_user
from django.urls import reverse
from django.conf import settings
from easy_thumbnails.files import get_thumbnailer


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = '태그 관리'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("instargram:tag_list", args=[self.pk])


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='my_post_set')
    photo = models.ImageField(upload_to='instargram/%Y/%m/%d', help_text='파일첨부는 필수 항목 입니다.')
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag_set = models.ManyToManyField(Tag, blank=True)
    location = models.CharField(max_length=50)
    like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='like_post_set')
    is_used = models.BooleanField(verbose_name='공개여부',default=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = '포스트 관리'

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse("instargram:post_detail", args=[self.pk])

    def extract_tag_list(self):
        tag_list = []
        tag_caption = re.findall(r"#[a-zA-Z\dㄱ-힣]+", self.caption)
        for tag_name in tag_caption:
            tags, _ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tags)
        return tag_list

    @property
    def caption_tag_links(self):
        '''
            태그에 링크를 걸어줄려고 합니다. 정규식으로 찾은 태그들을 
            replace 를 통해 문자열 변경 처리함
        '''
        caption_list = self.caption
        for tag in self.tag_set.all():
            url = tag.get_absolute_url()
            link = r"<a href='{url}' class='text-decoration-none'>{tagname}</a>".format(url=url, tagname=tag.name)
            caption_list = caption_list.replace(tag.name, link)
        return caption_list

    def post_is_used(self):
        return self.is_used

    @property
    def thumbnail_256(self):
        thumb = get_thumbnailer(self.photo)['thumb'].url
        return thumb

    @property
    def thumbnail_800(self):
        thumb = get_thumbnailer(self.photo)['posts'].url
        return thumb


class Comment(BaseModel):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_id')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    class Meta:
        ordering = '-created_at', '-updated_at'

    def __str__(self):
        return self.content
