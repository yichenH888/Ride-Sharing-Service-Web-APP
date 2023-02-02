from django.urls import path

from .views import driver_view

urlpatterns = [
    path('', driver_view, name='driver_view'),
]
