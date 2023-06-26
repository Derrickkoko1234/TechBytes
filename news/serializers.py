from rest_framework import serializers
from news.models import *


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
    def to_representation(self, instance):
        self.fields['article'] = ArticleSerializer(read_only=True)
        return super(CommentSerializer, self).to_representation(instance)
    

class MicroCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
    

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        
    def to_representation(self, instance):
        self.fields['article'] = ArticleSerializer(read_only=True)
        return super(LikeSerializer, self).to_representation(instance)

        
    