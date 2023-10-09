from rest_framework import viewsets

from ..models import Organization
from ..serializers import OrganizationSerializers

class OrganizationViewset(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializers