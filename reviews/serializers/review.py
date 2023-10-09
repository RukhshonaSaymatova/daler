from rest_framework import serializers
from ..models import Review

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review 
        fields = ('id', 'user', 'project', 'reviews_text', 'rating')