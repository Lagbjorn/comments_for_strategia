import uuid

from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from config.settings.base import MAX_COMMENT_LENGTH, MAX_NAME_LENGTH, MAX_TITLE_LENGTH, MAX_ARTICLE_LENGTH


class Article(models.Model):
    """Simple article placeholder"""
    article_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.CharField(max_length=MAX_NAME_LENGTH)
    title = models.CharField(max_length=MAX_TITLE_LENGTH)
    text = models.CharField(max_length=MAX_ARTICLE_LENGTH)
    published = models.DateTimeField(auto_now_add=True)


class Comment(MPTTModel):
    """
    Comment model with hierarchy based on MPTT algorithm. Read more here:
    https://django-mptt.readthedocs.io/en/latest/overview.html#what-is-modified-preorder-tree-traversal
    """
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    text = models.CharField(max_length=MAX_COMMENT_LENGTH)
    author = models.CharField(max_length=MAX_NAME_LENGTH)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    published = models.DateTimeField(auto_now_add=True)
