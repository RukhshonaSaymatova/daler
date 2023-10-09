from django.urls import path, include
from rest_framework import routers
from .views import ProjectViewset


router = routers.DefaultRouter()
router.register("project", ProjectViewset)

urlpatterns = [
    path("", include(router.urls)),
]