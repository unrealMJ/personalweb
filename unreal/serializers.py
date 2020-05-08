from rest_framework import serializers
from .models import *


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        depth = 0
        fields = ('id', 'title', 'date')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        depth = 0
        fields = '__all__'


class SecCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecComment
        depth = 0
        fields = '__all__'