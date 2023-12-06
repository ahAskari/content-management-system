from rest_framework import serializers

from post.serializers import PostSerializer
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = '__all__'
