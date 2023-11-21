from rest_framework import serializers


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
    photo = serializers.ImageField()
    created_at = serializers.DateField()
    author_id = serializers.IntegerField()
