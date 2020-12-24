from django.db import models
from django.contrib.auth.models import AbstractUser
#画像処理
from PIL import Image

# Create your models here.
class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""
    class Meta(AbstractUser.Meta):
        db_table = 'custom_user'

    bio = models.TextField(max_length=500, blank=True)
    age = models.IntegerField('何期生', blank=True, default=0)