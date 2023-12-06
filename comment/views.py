from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from comment.serializers import CommentSerializer
from comment.models import Comment
from django.http import Http404


class CommentView(APIView):
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
        except Comment.DoesNotExist:
            return Response(None, status.HTTP_404_NOT_FOUND)

    def get(self, request: Request):
        comment = self.get_object(request)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request):
        data = request.data
        data['author'] = request.user.pk
        serializer = CommentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class CommentDetailsView(APIView):
    serializer_class = CommentSerializer

    @extend_schema(
        request=CommentSerializer,
        responses={201: CommentSerializer},
        description='this api is used to get, update or delete comment by id'
    )
    def get_object(self, request: Request, pk: int):
        user_id = request.user.id

        try:
            return Comment.objects.get(author=user_id, pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request: Request, pk: int):
        comment = self.get_object(request, pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request: Request, pk: int):
        comment = self.get_object(request, pk)
        data = request.data
        data['author'] = request.user.pk
        serializer = CommentSerializer(comment, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int):
        comment = self.get_object(request, pk)
        comment.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)


class CommentOfArticle(APIView):
    serializer_class = CommentSerializer

    @extend_schema(
        request=CommentSerializer,
        responses={201: CommentSerializer},
        description='this api is used to get, update or delete comment by id'
    )
    def get_object(self, request: Request, pk: int):
        user_id = request.user.id

        try:
            return Comment.objects.filter(author=user_id, post=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request: Request, pk: int):
        comment = self.get_object(request, pk)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
