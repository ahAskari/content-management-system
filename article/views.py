from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from article.serializers import ArticleSerializer
from article.models import Article
from rest_framework import generics


class ArticlesView(APIView):
    serializer_class = ArticleSerializer

    @extend_schema(
        request=ArticleSerializer,
        responses={200: ArticleSerializer},
        description='this api is used to get all article or post new article'
    )
    def get_object(self, request: Request):
        user_id = request.user.id
        try:
            return Article.objects.filter(author=user_id)
        except:
            return Response(None, status.HTTP_404_NOT_FOUND)

    def get(self, request: Request):
        article = self.get_object(request)
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ArticleDetailsView(APIView):
    serializer_class = ArticleSerializer

    @extend_schema(
        request=ArticleSerializer,
        responses={201: ArticleSerializer},
        description='this api is used to get, update or delete article by id'
    )
    def get_object(self, request: Request, pk: int):
        user_id = request.user.id
        try:
            return Article.objects.filter(author=user_id, pk=pk)
        except Article.DoesNotExist:
            return Response(None, status.HTTP_404_NOT_FOUND)

    def get(self, request: Request, pk: int):
        article = self.get_object(request, pk)
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request: Request, pk: int):
        article = self.get_object(request, pk)
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int):
        article = self.get_object(request, pk)
        article.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)
