from django.urls import path

from api.v1 import views

urlpatterns = [
    path('comment/<uuid:pk>/', views.CommentView.as_view()),
    path('comment/', views.NewCommentView.as_view()),
    path('article/<uuid:pk>/', views.ArticleView.as_view()),
    path('article/', views.NewArticleView.as_view()),
]
