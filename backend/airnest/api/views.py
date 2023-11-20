from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .model import Proflie, Location, Sopt, Review, Booking, Image
from api.serializers import UserSerializer, ProfileSerializer, LocationSerializer, SpotSerializer, ReviewSerializer, BookingSerializer, ImageSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProfleViewSet(viewsets.ModelViewSet):
    queryset = Proflie.objects.all()
    serializer_class = ProflieSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class SpotViewSet(viewsets.ModelViewSet):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer