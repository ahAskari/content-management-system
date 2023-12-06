from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from tag.serializers import TagSerializer
from .models import Tag


class TagList(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
