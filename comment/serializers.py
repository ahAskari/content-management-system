from rest_framework import serializers


class CommentSerializer(serializers.Serializer):
    content = serializers.CharField()
    created_at = serializers.DateField()
    author_id = serializers.IntegerField()
