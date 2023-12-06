from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from post.models import Post
from post.serializers import PostSerializer


def store_file(file):
    with open('temp/image.jpg', 'wb+') as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class ArticlesView(APIView):
    serializer_class = PostSerializer

    @extend_schema(
        request=PostSerializer,
        responses={200: PostSerializer},
        description='this api is used to get all post or post new post'
    )
    def get_object(self, request: Request):
        user_id = request.user.id
        try:
            return Post.objects.filter(author=user_id)
        except Post.DoesNotExist:
            return Response(None, status.HTTP_404_NOT_FOUND)

    def get(self, request: Request):
        post = self.get_object(request)
        serializer = PostSerializer(post, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request):
        post = request.data
        post['author'] = request.user.pk
        serializer = PostSerializer(data=post)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ArticleDetailsView(APIView):
    serializer_class = PostSerializer

    @extend_schema(
        request=PostSerializer,
        responses={201: PostSerializer},
        description='this api is used to get, update or delete post by id'
    )
    def get_object(self, request: Request, pk: int):
        user_id = request.user.id

        try:
            return Post.objects.filter(author=user_id, pk=pk)
        except Post.DoesNotExist:
            return Response(None, status.HTTP_404_NOT_FOUND)

    def get(self, request: Request, pk: int):
        post = self.get_object(request, pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request: Request, pk: int):
        post = self.get_object(request, pk)
        data = request.data
        data['author'] = request.user.pk
        serializer = PostSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int):
        post = self.get_object(request, pk)
        post.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)
