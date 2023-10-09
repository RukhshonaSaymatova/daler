from rest_framework import viewsets

from ..models import Review
from ..serializers import ReviewSerializers

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers