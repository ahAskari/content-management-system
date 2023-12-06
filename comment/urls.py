from django.urls import path

from comment.views import CommentView, CommentDetailsView, CommentOfArticle


urlpatterns = [
    path('', CommentView.as_view()),
    path('<int:pk>', CommentDetailsView.as_view()),
    path('post/<int:pk>', CommentOfArticle.as_view()),
]
