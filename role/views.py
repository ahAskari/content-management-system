from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from role.serializers import RoleSerializer
from .models import Role


class RoleList(ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RoleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
