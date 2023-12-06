from django.urls import path
from tag.views import TagList, TagDetail

urlpatterns = [
    path('', TagList.as_view()),
    path('<int:pk>', TagDetail.as_view()),
]
