from django.urls import path, include
from rest_framework import routers
from .views import OrganizationViewset


router = routers.DefaultRouter()
router.register("organization", OrganizationViewset)


urlpatterns = [
    path("", include(router.urls)),
]