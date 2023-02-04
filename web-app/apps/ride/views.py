from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import DriverRegisterForm, DriverUpdateForm, RideRequestForm, RideUpdateForm
from .models import Driver, Ride, RideStatusType, RideShare


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
            # todo)) change all confirmed rides to open
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
            return redirect('ride_request_success_view')
    else:
        form = RideRequestForm()
    return render(request, 'ride/request.html', {'form': form})


@login_required(login_url="/register/")
def request_success_view(request):
    return render(request, 'ride/request_success.html')


@login_required(login_url="/register/")
def my_rides_view(request):
    # Get the selected status from the query string
    status = request.GET.get('status')
    driver = Driver.objects.filter(user=request.user).first()

    # Get all rides related to user
    sharerides = RideShare.objects.filter(sharer=request.user)
    # [debug]
    rides = Ride.objects.all()
    # rides = Ride.objects.filter(Q(owner=request.user) |
    #                             Q(driver=driver) |
    #                             Q(rideshare__in=sharerides))

    # rides += sharerides
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


@login_required(login_url="/register/")
def detail_view(request, pk):
    ride = get_object_or_404(Ride, pk=pk)

    is_driver = Driver.objects.filter(user=request.user).exists()
    is_driver_for_this_ride = ride.driver == request.user
    is_owner_for_this_ride = ride.owner == request.user
    is_sharer_for_this_ride = RideShare.objects.filter(ride=ride, sharer=request.user).exists()
    has_sharer = bool(RideShare.objects.filter(ride=ride))
    sharers = RideShare.objects.filter(ride=ride)

    show_driver_btn = is_driver \
                      and not is_driver_for_this_ride \
                      and ride.status == RideStatusType.OPEN \
                      and not is_owner_for_this_ride \
                      and not is_sharer_for_this_ride
    show_owner_btn = is_owner_for_this_ride \
                     and ride.status == RideStatusType.OPEN \
                     and not has_sharer
    show_sharer_btn = is_sharer_for_this_ride \
                      and ride.status == RideStatusType.OPEN
    show_join_btn = not is_owner_for_this_ride \
                    and not is_driver_for_this_ride \
                    and ride.status == RideStatusType.OPEN \
                    and ride.sharable \
                    and not is_sharer_for_this_ride

    return render(request, 'ride/detail.html', {'ride': ride,
                                                'sharers': sharers,
                                                'show_driver_btn': show_driver_btn,
                                                'show_owner_btn': show_owner_btn,
                                                'show_sharer_btn': show_sharer_btn,
                                                'show_join_btn': show_join_btn})


# todo)) fix ride.sharers -> RideShare
@login_required(login_url="/register/")
def cancel_view(request, pk):
    ride = get_object_or_404(Ride, pk=pk)
    if ride.sharers.contains(request.user):
        ride.sharers.remove(request.user)
        ride.save()
    elif ride:
        ride.delete()
        ride.save()
    return render(request, 'ride/cancel.html')


@login_required(login_url="/register/")
def join_view(request, pk):
    ride = get_object_or_404(Ride, pk=pk)
    passenger_count = RideShare.objects.filter(ride=ride,
                                               sharer=request.user).first().passenger_count if RideShare.objects.filter(
        ride=ride, sharer=request.user).exists() else 1

    if request.method == 'POST':
        ride.add_sharer(request.user, request.POST.get('passenger_count'))
        return redirect('ride_join_success_view')
    # else:
    #     exist_rideshare = RideShare.objects.filter(ride=ride, sharer=request.user).first()
    #     if exist_rideshare:
    #         passenger_count = exist_rideshare.passenger_count
    return render(request, 'ride/join.html', {'passenger_count': passenger_count})


@login_required(login_url="/register/")
def join_success_view(request):
    return render(request, 'ride/join_success.html')


@login_required(login_url="/register/")
def confirm_view(request, pk):
    # Get the current user's Driver instance
    driver = Driver.objects.filter(user=request.user).first()
    # get the ride object
    ride = get_object_or_404(Ride, pk=pk)
    # check if the user is a driver and the ride is open
    # todo)) check the number of passenger is satisfied
    if driver and ride.status == RideStatusType.OPEN:
        # update the ride status and driver
        ride.status = RideStatusType.CONFIRMED
        ride.driver = driver
        ride.save()
        messages.success(request, 'Order confirmed!')
    return redirect('ride_detail_view', pk=ride.pk)


@login_required(login_url="/register/")
def update_view(request, pk):
    ride = get_object_or_404(Ride, pk=pk)

    if request.method == "POST":
        form = RideUpdateForm(request.POST, instance=ride)
        if form.is_valid():
            ride = form.save()
            return redirect('ride_detail_view', pk=ride.pk)
    else:
        form = RideUpdateForm(instance=ride)
    return render(request, 'ride/update.html', {'form': form})
