from django.urls import path, include
from rest_framework import routers
from .views import ParticipationViewset


router = routers.DefaultRouter()
router.register("participation", ParticipationViewset)


urlpatterns = [
    path("", include(router.urls)),
]