from django.urls import include, path
from rest_framework.routers import DefaultRouter
from user.views import Author, UserView, UsersViewset


router = DefaultRouter()
router.register('', UsersViewset)

urlpatterns = [
    # path('', include(router.urls)),
    path('', UserView.as_view()),
    path('author', Author.as_view()),
]
