from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProfileViewSet, LocationViewSet, SpotViewSet, ReviewViewSet, BookingViewSet, ImageViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet, basename='profile')
router.register(r'locations', LocationViewSet, basename='location')
router.register(r'spots', SpotViewSet, basename='spot')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'bookings', BookingViewSet, basename='booking')
router.register(r'images', ImageViewSet, basename='image')

urlpatterns = [
    path('', include(router.urls)),
]