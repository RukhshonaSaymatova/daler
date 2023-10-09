from rest_framework import serializers
from ..models import Participation

class ParticipationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = ('id', 'user', 'project', 'dt_of_joining', 'dt_of_departure')