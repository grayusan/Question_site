from users.models import CustomUser
from django.conf import settings
from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField
from django.urls import reverse


#https://blog.narito.ninja/detail/173/
#上記の記事参照。タグの追加により記事の検索を楽にする
'''
class Tag(models.Model):
    name = models.CharField('タグ名', max_length=255, unique=True)

    def __str__(self):
        return self.name
'''


class Post(models.Model):
    title = models.CharField(max_length=70)
    text = MarkdownxField('本文', help_text='Markdown形式で書いてください。')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    #tags = models.ManyToManyField(Tag, verbose_name='タグ', blank=True)

    description = models.TextField('記事の説明', max_length=130)
    updated_at = models.DateTimeField('更新日', default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('situmon:situmon-home')

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    """コメント."""
    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = MarkdownxField('コメント本文', help_text='Markdown形式で書いてください。')
    target = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField('作成日', default=timezone.now)
 
    def __str__(self):
        return self.name
 
 
class Reply(models.Model):
    """返信コメント."""
    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = MarkdownxField('返信本文', help_text='Markdown形式で書いてください。')
    target = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.name
    
'''
#コメント欄の実装
class Comment(models.Model):
    """記事に紐づくコメント"""
    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField('本文', null=True)
    target = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='対象記事')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.text[:20]

class Reply(models.Model):
    """コメントに紐づく返信"""
    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField('本文', null=True)
    target = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name='対象コメント')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.text[:20]
'''