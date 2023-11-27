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

    # def validate_content(self, content):
    #     min_character = 10
    #     if len(content) < min_character :
    #         raise serializers.ValidationError(f'your content should be greater than {min_character}')
    #     return content
