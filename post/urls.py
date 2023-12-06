from django.urls import path
from post.views import ArticleDetailsView, ArticlesView

urlpatterns = [
    path('', ArticlesView.as_view()),
    path('<int:pk>', ArticleDetailsView.as_view()),
]
