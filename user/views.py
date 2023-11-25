from rest_framework import viewsets
from user.serializers import UserSerializer
from .models import User


class UsersViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
