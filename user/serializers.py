from rest_framework import serializers

from article.serializers import ArticleSerializer
from .models import User


class UserSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = '__all__'
