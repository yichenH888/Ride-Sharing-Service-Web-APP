from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.utils import timezone


# Helper functions
class VehicleType(models.TextChoices):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    MPV = 'MPV'
    OTHER = 'Other'


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
    max_capacity = models.PositiveIntegerField(default=3)
    vehicle_type = models.CharField(max_length=100,
                                    blank=True,
                                    choices=VehicleType.choices,
                                    default=VehicleType.SEDAN)

    def __str__(self):
        return self.user.username


class Ride(models.Model):
    # Binding Users
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, related_name="driver")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    # sharers = models.ManyToManyField(User, related_name="sharer", blank=True)
    # Ride info
    sharable = models.BooleanField(default=True)
    destination = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    arrive_time = models.DateTimeField(default=timezone.now)
    passengers_count = models.PositiveIntegerField(default=1)
    total_passengers = models.PositiveIntegerField(default=1)
    vehicle_type = models.CharField(max_length=100, blank=False, choices=VehicleType.choices,
                                    default=VehicleType.SEDAN)
    status = models.CharField(max_length=100, choices=RideStatusType.choices, default=RideStatusType.OPEN)
    additional_requests = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.destination

    def add_sharer(self, user, passenger_count):
        rideshare = RideShare.objects.filter(ride=self, sharer=user).first()
        if rideshare:
            rideshare.passenger_count = passenger_count
            rideshare.save()
        else:
            RideShare.objects.create(ride=self, sharer=user, passenger_count=passenger_count)
        self.update_total_passengers()

    def remove_sharer(self, user):
        RideShare.objects.filter(ride=self, sharer=user).delete()
        self.update_total_passengers()

    def update_total_passengers(self):
        rideshare_count = RideShare.objects.filter(ride=self).aggregate(Sum('passenger_count'))[
                              'passenger_count__sum'] or 0
        self.total_passengers = rideshare_count + self.passengers_count
        self.save()


class RideShare(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='rideshare')
    sharer = models.ForeignKey(User, on_delete=models.CASCADE)
    passenger_count = models.PositiveIntegerField()
