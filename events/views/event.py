from rest_framework import viewsets

from ..models import Event
from ..serializers import EventSerializers

class EventViewset(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializers