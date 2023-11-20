from django.db import models


class Profile(models.Model):
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Location(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    lat = models.IntegerField()
    lng = models.IntegerField()

class Spot(models.Model):
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    address = models.ForeignKey(Location, on_delete=models.CASCADE)

class Review(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
    review = models.TextField()
    stars = models.IntegerField()

class Booking(models.Model):
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class Image(models.Model):
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True, blank=True)
    url = models.CharField(max_length=255)
