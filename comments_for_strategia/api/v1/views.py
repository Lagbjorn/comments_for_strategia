from mptt.templatetags.mptt_tags import cache_tree_children
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.serializers import ArticleSerializer, CommentSerializer
from comments.models import Article, Comment


class NewView(APIView):
    """Abstract class for posting instances to keep it DRY"""
    serializer = None

    def post(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ArticleView(APIView):
    def get(self, request, pk):
        article = Article.objects.get(article_id=pk)
        serializer = ArticleSerializer(article, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentView(APIView):
    def get(self, request, pk):
        comment_tree = Comment.objects.get(comment_id=pk).get_descendants(include_self=True)
        comment_tree = cache_tree_children(comment_tree)
        serializer = CommentSerializer(comment_tree[0])
        return Response(serializer.data, status=status.HTTP_200_OK)


class NewCommentView(NewView):
    serializer = CommentSerializer


class NewArticleView(NewView):
    serializer = ArticleSerializer
