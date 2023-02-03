from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import DriverRegisterForm, DriverUpdateForm, RideRequestForm
from .models import Driver, Ride, RideStatusType


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


@login_required(login_url="/register/")
def request_view(request):
    if request.method == 'POST':
        form = RideRequestForm(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.owner = request.user
            ride.status = 'open'
            ride.save()
            form.save_m2m()
            return redirect('request_success_view')
    else:
        form = RideRequestForm()
    return render(request, 'ride/request.html', {'form': form})


@login_required(login_url="/register/")
def request_success_view(request):
    return render(request, 'ride/request_success.html')


def my_rides_view(request):
    # Get the selected status from the query string
    status = request.GET.get('status')
    # Get all rides by default
    rides = Ride.objects.all()
    # Filter rides by status if the status is not "All"
    if status and status != 'all':
        rides = rides.filter(status=status)
    context = {
        'rides': rides,
        'status': status,
        'status_choices': RideStatusType.choices
    }
    # Render the ride list template with the context
    return render(request, 'ride/my_rides.html', context)
#
# @login_required
# def ride_update(request, pk):
#     ride = Ride.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = RideUpdateForm(request.POST, instance=ride)
#         if form.is_valid():
#             ride = form.save()
#             return redirect('ride_list')
#     else:
#         form = RideUpdateForm(instance=ride)
#     context = {'form': form, 'ride': ride}
#     return render(request, 'rides/ride_update.html', context)
