from rest_framework import viewsets

from ..models import Participation
from ..serializers import ParticipationSerializers

class ParticipationViewset(viewsets.ModelViewSet):
    queryset = Participation.objects.all()
    serializer_class = ParticipationSerializers