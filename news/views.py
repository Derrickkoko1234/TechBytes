from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from news.serializers import *

# Create your views here.


@api_view(['POST'])
@permission_classes((IsAdminUser, ))
def create_article(request):
    context = {}
    article_serializer = ArticleSerializer(data=request.data)
    if article_serializer.is_valid():
        article_serializer.save()
        context['message'] = "Article saved successfully"
        return Response(context, status.HTTP_201_CREATED)
    else:
        return Response(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_articles(request):
    context = {}
    articles = Article.objects.filter(is_public=True)
    articles_serializer = ArticleSerializer(
        articles, many=True).order_by('date_time_created')
    context['articles'] = articles_serializer.data
    return Response(context, status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_article_details(request, slug):
    context = {}
    check_article = Article.objects.filter(slug=slug, is_public=True).count()
    if check_article == 0:
        context['message'] = "Article not found"
        return Response(context, status.HTTP_400_BAD_REQUEST)
    else:
        article = Article.objects.get(slug=slug, is_public=True)
        article_serializer = ArticleSerializer(article, many=False)
        context['article'] = article_serializer.data
        
        likes = Like.objects.filter(article=article).count()
        context['likes'] = likes
        
        comments = Comment.objects.filter(article=article).count()
        context['comments'] = comments
        
        return Response(context, status.HTTP_200_OK)

