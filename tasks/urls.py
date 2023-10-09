from django.urls import path, include
from rest_framework import routers
from .views import TaskViewset


router = routers.DefaultRouter()
router.register("task", TaskViewset)


urlpatterns = [
    path("", include(router.urls)),
]