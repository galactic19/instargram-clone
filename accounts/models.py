from tabnanny import verbose
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.shortcuts import resolve_url
from easy_thumbnails.files import get_thumbnailer
from django.db.models import Q


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = 'M', '남성'
        FEMALE = 'F', '여성'

    follower_set = models.ManyToManyField('self', blank=True, symmetrical=False,
                                          related_name='following',)
    following_set = models.ManyToManyField('self', blank=True, symmetrical=False,
                                           related_name='follower',)

    profile_image = models.ImageField(upload_to='profile/image/%Y/%m/%d', blank=True, verbose_name='프로필 이미지',
                                      help_text='프로필 이미지의 크기는 24x24 입니다.')
    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")],
                                    max_length=13,
                                    blank=True,
                                    verbose_name='휴대전화',
                                    help_text='휴대전화 번호를 입력하세요')

    gender = models.CharField(max_length=1,
                              blank=True,
                              choices=GenderChoices.choices,
                              verbose_name='성별',
                              help_text='성별을 선택하세요')

    def _str__(self):
        return self.username

    @property
    def user_profile_image_url(self):
        try:
            img = get_thumbnailer(self.profile_image)['avatar'].url
        except:
            img = resolve_url('pydenticon_image', self.username)
            # img = get_thumbnailer(img)['avatar'].url
        return img

    @property
    def user_profile_image_250(self):
        try:
            img = get_thumbnailer(self.profile_image)['profile'].url
        except:
            img = resolve_url('pydenticon_image', self.username)
        return img