from rest_framework import serializers
from ..models import Organization

class OrganizationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'name', 'description', 'project')