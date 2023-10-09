from django.urls import path, include
from rest_framework import routers
from .views import ReviewViewset


router = routers.DefaultRouter()
router.register("review", ReviewViewset)


urlpatterns = [
    path("", include(router.urls)),
]