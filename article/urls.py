from django.urls import path
from article.views import ArticleDetailsView, ArticlesView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', ArticlesView.as_view()),
    path('<int:pk>', ArticleDetailsView.as_view()),
    path('auth-token/', obtain_auth_token, name='generate_auth_token')
]
