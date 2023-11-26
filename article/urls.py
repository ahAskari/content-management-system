from django.urls import include, path
from article.views import ArticlesView, article_detail_view, articles_view, ArticleDetailsView, ArticleGenericDetailView, ArticleViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('', ArticleViewSet, basename='articleViewSet')

urlpatterns = [
    path('', ArticlesView.as_view()),
    path('<int:pk>', ArticleDetailsView.as_view()),
    path('', articles_view),
    path('<int:pk>', article_detail_view),
    path('generic/<int:pk>', ArticleGenericDetailView.as_view()),
    path('viewsets/', include(router.urls)),
    path('auth-token/', obtain_auth_token, name='generate_auth_token')
]
