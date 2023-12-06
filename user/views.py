from drf_spectacular.utils import extend_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from user.serializers import UserSerializer
from .models import User


class UsersViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserView(APIView):
    serializer_class = UserSerializer

    @extend_schema(
        request=UserSerializer,
        responses={201: UserSerializer},
    )
    def get_object(self, request: Request):
        user_id = request.user.id
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(None, status.HTTP_404_NOT_FOUND)

    def get(self, request: Request):
        user = self.get_object(request)
        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, request: Request):
        user = self.get_object(request)
        serializer = UserSerializer(user, data=request.user)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request):
        user = self.get_object(request)
        user.delete()

        return Response(None, status.HTTP_204_NO_CONTENT)


class Author(ListAPIView):
    queryset = User.objects.filter(role__name__in=['admin', 'editor'])
    serializer_class = UserSerializer
