from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, mixins, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from article.serializers import ArticleSerializer
from article.models import Article

# region functional view


@api_view(['GET', 'POST'])
def articles_view(request: Request):
    try:
        article = Article.objects.all()
    except:
        return Response(None, status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        return Response(serializer.data, status.HTTP_201_CREATED)

    return Response(None, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_view(request: Request, pk: int):

    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(None, status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(None, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)
    else:
        return Response(None, status.HTTP_400_BAD_REQUEST)
# endregion


# region class view
class ArticlesView(APIView):
    def get_object(self):
        try:
            return Article.objects.all()
        except:
            return Response(None, status.HTTP_404_NOT_FOUND)

    def get(self, request):
        article = self.get_object()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(None, status.HTTP_400_BAD_REQUEST)


class ArticleDetailsView(APIView):

    def get_object(self, pk: int):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response(None, status.HTTP_404_NOT_FOUND)

    def get(self, request: Request, pk: int):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request: Request, pk: int):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(None, status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int):
        article = self.get_object(pk)
        article.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)
# endregion


# region mixin
class ArticleMixinDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request: Request, pk: int):
        return self.retrieve(request, pk)

    def put(self, request: Request, pk):
        return self.update(request, pk)

    def delete(self, request: Request, pk):
        return self.destroy(request, pk)
# endregion


# region generic
class ArticleGenericDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
# endregion


# region viewsets
class PaginationApiView(LimitOffsetPagination):
    page_size = 1


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = PaginationApiView
# endregion
