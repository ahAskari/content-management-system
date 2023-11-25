from django.urls import include, path
from rest_framework.routers import DefaultRouter
from user.views import UsersViewset


router = DefaultRouter()
router.register('', UsersViewset)

urlpatterns = [
    path('', include(router.urls))
]
