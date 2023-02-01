from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Helper functions
class VehicleType(models.TextChoices):
    SEDAN = 'sedan'
    SUV = 'suv'
    MPV = 'mpv'
    OTHER = 'other'


class RideStatusType(models.TextChoices):
    OPEN = 'open'
    CONFIRMED = 'confirmed'
    COMPLETED = 'completed'
    CANCELED = 'canceled'


class Driver(models.Model):
    # Related user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Vehicle info
    plate_number = models.CharField(max_length=10)
    max_cap = models.PositiveIntegerField(default=3)
    vehicle_type = models.CharField(max_length=100,
                                    blank=True,
                                    choices=VehicleType.choices,
                                    default=VehicleType.SEDAN)

    def __str__(self):
        return self.plate_number


class Ride(models.Model):
    # Binding Users
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, blank=True, null=True, related_name="driver")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    sharer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sharer")
    # Ride info
    sharable = models.BooleanField(default=True)
    destination = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    arrive_time = models.DateTimeField(default=timezone.now())
    total_passenger = models.PositiveIntegerField(default=1)
    vehicle_type = models.CharField(max_length=100, blank=True, choices=VehicleType.choices,
                                    default=VehicleType.SEDAN)
    status = models.CharField(max_length=100, choices=RideStatusType.choices, default=RideStatusType.OPEN)
    other_request = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.destination
