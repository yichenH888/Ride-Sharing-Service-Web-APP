from django.urls import path

from .views import login_view, register_user, logout_view

urlpatterns = [
    path('register/', register_user, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name='logout'),
]
