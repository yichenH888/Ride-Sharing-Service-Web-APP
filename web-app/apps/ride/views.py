from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import DriverRegisterForm, DriverUpdateForm
from .models import Driver


# @login_required(login_url="/login/")
# def driver_register(request):
#     if request.method == 'POST':
#         # Check if the user has already registered as a driver
#         driver = Driver.objects.filter(user=request.user).first()
#         if driver:
#             messages.error(request, 'You are already a driver')
#             return redirect('/')
#
#         form = DriverRegisterForm(request.POST)
#         if form.is_valid():
#             # Save the driver data but do not commit it to the database yet
#             driver = form.save(commit=False)
#             driver.user = request.user
#             driver.save()
#             return redirect('/')
#     else:
#         form = DriverRegisterForm()
#
#     return render(request, 'ride/driver.html', {'form': form})
#
#
# @login_required(login_url="/login/")
# def driver_update(request):
#     # Retrieve the current driver object related to the logged-in user
#     driver = Driver.objects.get(user=request.user)
#
#     # Create an instance of DriverUpdateForm with the current driver data
#     form = DriverUpdateForm(instance=driver)
#
#     if request.method == 'POST':
#         # Update the form instance with the new data submitted through the form
#         form = DriverUpdateForm(request.POST, instance=driver)
#         if form.is_valid():
#             # Save the updated data to the database
#             form.save()
#             messages.success(request, 'Driver information updated successfully')
#             return redirect('ride:driver')
#
#     # Render the driver_update.html template with the updated form instance
#     return render(request, 'ride/driver_update.html', {'form': form})

@login_required(login_url="/register/")
def driver_view(request):
    # Get the current user's Driver instance
    driver = Driver.objects.filter(user=request.user).first()
    # A flag to determine if the update form should be displayed
    show_form = False

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
            if 'unregister' in request.POST:
                driver.delete()
                return redirect('driver_view')
            form = DriverUpdateForm(request.POST, instance=driver)
            if form.is_valid():
                form.save()
                return redirect('driver_view')
    else:
        if driver is not None:
            form = DriverUpdateForm(instance=driver)
        else:
            form = DriverRegisterForm()

    if request.method == 'POST':
        # Check if the update form should be displayed
        if 'update' in request.POST:
            show_form = True
            form = DriverUpdateForm(instance=driver)

    return render(request, 'ride/driver.html', {'form': form,
                                                'driver': driver,
                                                'show_form': show_form})
