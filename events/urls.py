from django.urls import path, include
from rest_framework import routers
from .views import EventViewset


router = routers.DefaultRouter()
router.register("event", EventViewset)


urlpatterns = [
    path("", include(router.urls)),
]