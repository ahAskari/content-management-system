from rest_framework import serializers
from article.models import Article


# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     content = serializers.CharField()
#     photo = serializers.ImageField()
#     created_at = serializers.DateField()
#     author_id = serializers.IntegerField()

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
