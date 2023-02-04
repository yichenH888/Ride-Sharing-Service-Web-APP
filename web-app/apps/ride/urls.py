from django.urls import path

from .views import driver_view, request_view, request_success_view, my_rides_view, detail_view, confirm_view, \
    update_view, cancel_view, join_view, join_success_view

urlpatterns = [
    path('driver/', driver_view, name='driver_view'),
    path('request/', request_view, name='ride_request_view'),
    path('request_success/', request_success_view, name='ride_request_success_view'),
    path('my_rides/', my_rides_view, name='my_rides_view'),
    path('<int:pk>/', detail_view, name='ride_detail_view'),
    path('<int:pk>/confirm/', confirm_view, name='ride_confirm_view'),
    path('<int:pk>/update/', update_view, name='ride_update_view'),
    path('<int:pk>/cancel', cancel_view, name='ride_cancel_view'),
    path('<int:pk>/join', join_view, name='ride_join_view'),
    path('join_success/', join_success_view, name='ride_join_success_view'),
]
