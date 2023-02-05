from django.urls import path

from .views import profile_view, update_info_view, change_password_view

urlpatterns = [
    path('profile/', profile_view, name='accounts_profile_view'),
    path('update_info/', update_info_view, name='accounts_update_info_view'),
    path('change_password/', change_password_view, name='accounts_change_password_view'),
]
