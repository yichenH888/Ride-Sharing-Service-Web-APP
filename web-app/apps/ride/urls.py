from django.urls import path

from .views import driver_view, request_view, request_success_view, my_rides_view

urlpatterns = [
    path('driver/', driver_view, name='driver_view'),
    path('request/', request_view, name='ride_request_view'),
    path('request_success/', request_success_view, name='ride_request_success_view'),
    path('my_rides/', my_rides_view, name='my_rides_view'),
]
