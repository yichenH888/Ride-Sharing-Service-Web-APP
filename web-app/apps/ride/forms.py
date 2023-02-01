from django import forms
from django.contrib.auth.models import User

from .models import Driver, Ride


class RideRequestForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['sharable',
                  'destination',
                  'arrive_time',
                  'total_passenger',
                  'vehicle_type',
                  'other_request']


class RideUpdateForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['sharable',
                  'destination',
                  'arrival_time',
                  'total_passenger',
                  'vehicle_type',
                  'other_request']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class DriverRegisterForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['plate_number',
                  'max_cap',
                  'vehicle_type']


class DriverUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['plate_number',
                  'max_cap',
                  'vehicle_type']


class RideSearchForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['destination',
                  'arrival_time',
                  'vehicle_type',
                  'total_passenger']
