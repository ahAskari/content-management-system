from rest_framework import serializers

from post.models import Post
from comment.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.SerializerMethodField()
    author_avatar = serializers.SerializerMethodField()
    comment_post = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def get_author_username(self, obj):
        return obj.author.username if obj.author else None

    def get_author_avatar(self, obj):
        return obj.author.avatar if obj.author else None

    # def validate_content(self, content):
    #     min_character = 10
    #     if len(content) < min_character :
    #         raise serializers.ValidationError(f'your content should be greater than {min_character}')
    #     return content

    # def validate_content(self, content):
    #     min_character = 10
    #     if len(content) < min_character :
    #         raise serializers.ValidationError(f'your content should be greater than {min_character}')
    #     return content
