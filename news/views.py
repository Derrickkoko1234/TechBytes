from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

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
    articles = Article.objects.filter(
        is_public=True).order_by('date_time_created')
    articles_serializer = ArticleSerializer(
        articles, many=True)
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

        comments_count = Comment.objects.filter(article=article).count()
        context['comments_count'] = comments_count

        comments = Comment.objects.filter(
            article=article).order_by('date_time_created')
        context['comments'] = comments

        return Response(context, status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def create_comment(request):
    context = {}
    comment_serializer = CommentSerializer(data=request.data)
    if comment_serializer.is_valid():
        comment_serializer.save()
        context['message'] = "Comment saved successfully"
        return Response(context, status.HTTP_201_CREATED)
    else:
        return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def create_like(request):
    context = {}
    profile_id = request.data['profile']
    article_id = request.data['article']
    check_article = Article.objects.filter(id=article_id).count()
    if check_article == 0:
        context['message'] = "Article not found"
        return Response(context, status.HTTP_400_BAD_REQUEST)
    else:
        article = Article.objects.get(id=article_id)
        check_profile = Profile.objects.filter(id=profile_id).count()
        if check_profile == 0:
            context['message'] = "Profile not found"
            return Response(context, status.HTTP_400_BAD_REQUEST)
        else:
            profile = Profile.objects.get(id=profile_id)
            check_like = Like.objects.filter(
                profile=profile, article=article_id).count()
            if check_like == 0:
                like_serializer = LikeSerializer(data=request.data)
                if like_serializer.is_valid():
                    like_serializer.save()
                    context['message'] = "Like saved successfully"
                    return Response(context, status.HTTP_201_CREATED)
                else:
                    return Response(like_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                like = Like.objects.get(profile=profile, article=article_id)
                like.delete()
                context['message'] = "Like removed successfully"
                return Response(context, status.HTTP_200_OK)

