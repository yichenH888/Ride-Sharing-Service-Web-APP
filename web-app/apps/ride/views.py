from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.shortcuts import render, redirect

from .forms import DriverRegisterForm
from .models import Driver


@login_required(login_url="/login/")
def driver_register(request):
    driver_register_form = DriverRegisterForm()
    if request.method == 'POST':
        driver = Driver.objects.filter(user=request.user).first()
        if driver is not None:
            messages.error(request, 'You are already a driver')
            return render(request, 'ride/driver.html', {'form': driver_register_form})
        else:
            if driver_register_form.is_valid():
                driver = driver_register_form.save(commit=False)
                driver.user = request.user
                driver_register_form.save()
                return redirect('/')
    return render(request, 'ride/driver.html', {'form': driver_register_form})
