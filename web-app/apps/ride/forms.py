from django import forms
from django.contrib.auth.models import User

from .models import Driver, Ride, RideShare


class RideRequestForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['sharable',
                  'destination',
                  'arrive_time',
                  'passengers_count',
                  'vehicle_type',
                  'additional_requests']


class RideUpdateForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['sharable',
                  'destination',
                  'arrive_time',
                  'passengers_count',
                  'vehicle_type',
                  'additional_requests']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class DriverRegisterForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['plate_number',
                  'max_capacity',
                  'vehicle_type']


class DriverUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['plate_number',
                  'max_capacity',
                  'vehicle_type']


class RideSearchForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['destination',
                  'arrive_time',
                  'vehicle_type',
                  'passengers_count']


class RideJoinForm(forms.ModelForm):
    class Meta:
        model = RideShare
        fields = ['passenger_count']
