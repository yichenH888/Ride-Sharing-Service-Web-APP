from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import DriverRegisterForm, DriverUpdateForm
from .models import Driver


@login_required(login_url="/register/")
def driver_view(request):
    # Get the current user's Driver instance
    driver = Driver.objects.filter(user=request.user).first()
    # A flag to determine if the update form should be displayed
    show_form = False

    # Handle POST request
    if request.method == 'POST':
        # If the user has not registered as a Driver
        if driver is None:
            form = DriverRegisterForm(request.POST)
            if form.is_valid():
                driver = form.save(commit=False)
                driver.user = request.user
                driver.save()
                return redirect('driver_view')
        # If the user has registered as a Driver
        else:
            # Handle the 'cancel' button press
            if 'cancel' in request.POST:
                return redirect('driver_view')
            # Handle the 'unregister' button press
            if 'unregister' in request.POST:
                driver.delete()
                return redirect('driver_view')
            form = DriverUpdateForm(request.POST, instance=driver)
            if form.is_valid():
                form.save()
                return redirect('driver_view')
    # Handle GET request
    else:
        # If the user has registered as a Driver
        # Show the driver update form
        if driver is not None:
            form = DriverUpdateForm(instance=driver)
        # If the user has not registered as a Driver
        # Show the driver register form
        else:
            form = DriverRegisterForm()

    if request.method == 'POST':
        # Handle the 'update' button press
        if 'update' in request.POST:
            show_form = True
            form = DriverUpdateForm(instance=driver)

    return render(request, 'ride/driver.html', {'form': form,
                                                'driver': driver,
                                                'show_form': show_form})
