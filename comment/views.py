from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, generics
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from article.serializers import ArticleSerializer
from comment.serializers import CommentSerializer
from comment.models import Comment


class CommentsById(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    @extend_schema(
        request=CommentSerializer,
        responses={200: CommentSerializer},
        description='this api is used to get all comment or post new comment'
    )
    def get_queryset(self):
        user_id = self.request.user.pk
        return Comment.objects.filter(author=user_id)


class CommentsView(APIView):
    serializer_class = CommentSerializer

    @extend_schema(
        request=CommentSerializer,
        responses={200: CommentSerializer},
        description='this api is used to get all comment or post new comment'
    )
    def get_object(self, request: Request):
        user_id = request.user.id
        try:
            return Comment.objects.filter(author=user_id)
        except:
            return Response(None, status.HTTP_404_NOT_FOUND)

    def get(self, request: Request):
        comment = self.get_object(request)
        serializer = CommentSerializer(article, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ArticleDetailsView(APIView):
    serializer_class = CommentSerializer

    @extend_schema(
        request=CommentSerializer,
        responses={201: CommentSerializer},
        description='this api is used to get, update or delete article by id'
    )
    def get_object(self, request: Request, pk: int):
        user_id = request.user.id
        try:
            return Comment.objects.filter(author=user_id, pk=pk)
        except Comment.DoesNotExist:
            return Response(None, status.HTTP_404_NOT_FOUND)

    def get(self, request: Request, pk: int):
        article = self.get_object(request, pk)
        serializer = CommentSerializer(article, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request: Request, pk: int):
        article = self.get_object(request, pk)
        serializer = CommentSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int):
        article = self.get_object(request, pk)
        article.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)
