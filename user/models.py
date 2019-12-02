from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    type = models.CharField(max_length=30)
    #type = (
     #   ('G', 'Google'),
      #  ('K', 'KakaoTalk'),
    #)

    img_profile = models.ImageField('프로필 이미지', blank=True, upload_to='user/profile')
    oauth_token = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.username
