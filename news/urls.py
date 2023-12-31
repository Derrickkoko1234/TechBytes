from django.urls import path
from . import views

urlpatterns = [
    path('create-article', views.create_article, name='create-article'),
    path('get-articles', views.get_articles, name='get-articles'),
    path('get-article-details/<slug:slug>',
         views.get_article_details, name='get-article-details'),
    path('create-comment', views.create_comment, name='create-comment'),
    path('like-article', views.create_like, name='like-article'),
]
