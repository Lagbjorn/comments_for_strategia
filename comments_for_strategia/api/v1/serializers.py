from mptt.templatetags.mptt_tags import cache_tree_children

from comments.models import Article, Comment
from rest_framework import serializers
from django.conf import settings


class CommentSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField('get_children')
    article = serializers.PrimaryKeyRelatedField(queryset=Article.objects.all())
    parent = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), required=False)

    def get_children(self, comment):
        """
        Recursively get all children of the comment.
        You should cache your comment tree queryset before serializing to avoid N+1 queries problem.
        """
        max_depth = self.context.get('max_depth')
        _children = comment.get_children()
        if (max_depth is not None) and (comment.get_level() >= max_depth):
            return []
        return CommentSerializer(_children, many=True, context={'max_depth': max_depth}).data

    class Meta:
        model = Comment
        exclude = ('lft', 'rght', 'tree_id')
        read_only_fields = ('lft', 'rght', 'tree_id', 'level', 'children')


class ArticleSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField('get_comments')

    def get_comments(self, article):
        """Get comments with level no more than TREE_DEPTH"""
        _comments = cache_tree_children(Comment.objects.filter(article=article, level__lte=settings.TREE_DEPTH))
        serializer = CommentSerializer(_comments,
                                       many=True,
                                       context={'max_depth': settings.TREE_DEPTH},
                                       )
        return serializer.data

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('comments', 'published', 'article_id', )
