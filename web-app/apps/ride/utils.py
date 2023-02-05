from django.conf import settings
from django.core.mail import send_mail

SUBJECT_REGISTERED = "Welcome to RideConnect!"
SUBJECT_RIDE_CONFIRMED = "RideConnect - Ride Confirmed!"
SUBJECT_RIDE_CANCELED = "RideConnect - Ride Canceled!"
SUBJECT_RIDE_JOINED = "RideConnect - Ride Joined!"
SUBJECT_RIDE_COMPLETED = "RideConnect - Ride Completed!"
SUBJECT_RIDE_CHANGED = "RideConnect - Ride Changed!"


def send_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        recipient_list,
        fail_silently=False,
    )


def get_registered_body(user):
    return f"Dear {user.username},\n\nThank you for joining our site.\n\nBest regards,\nRideConnect"


def get_confirmed_body(user, ride):
    return f"Dear {user.username},\n" \
           f"\n" \
           f"Your ride has been confirmed.\n" \
           f"Your driver: {ride.driver}\n" \
           f"Plate #: {ride.driver.plate_number}\n" \
           f"Contact: {ride.driver.user.email}\n" \
           f"\n" \
           f"Best regards,\n" \
           f"RideConnect"


def get_canceled_body(user, ride):
    return f"Dear {user.username},\n" \
           f"\n" \
           f"Your ride has been canceled.\n" \
           f"Ride Information: \n" \
           f"Creat time: {ride.create_time}\n" \
           f"Destination: {ride.destination}\n" \
           f"Arrive time: {ride.arrive_time}\n" \
           f"\n" \
           f"Best regards,\n" \
           f"RideConnect"


def get_joined_body(user, ride, sharer):
    return f"Dear {user.username},\n" \
           f"\n" \
           f"A new sharer, {sharer.username}, has joined your ride.\n" \
           f"Ride Information: \n" \
           f"Creat time: {ride.create_time}\n" \
           f"Destination: {ride.destination}\n" \
           f"Arrive time: {ride.arrive_time}\n" \
           f"Total passengers: {ride.total_passengers}\n" \
           f"\n" \
           f"Best regards,\n" \
           f"RideConnect"


def get_completed_body(ride):
    return f"Dear user,\n" \
           f"\n" \
           f"Your ride has been completed.\n" \
           f"Ride Information: \n" \
           f"Creat time: {ride.create_time}\n" \
           f"Destination: {ride.destination}\n" \
           f"Arrive time: {ride.arrive_time}\n" \
           f"Total passengers: {ride.total_passengers}\n" \
           f"\n" \
           f"Best regards,\n" \
           f"RideConnect"


def get_changed_body(ride):
    return f"Dear user,\n" \
           f"\n" \
           f"Your ride has been Changed.\n" \
           f"Ride Information: \n" \
           f"Creat time: {ride.driver}\n" \
           f"Creat time: {ride.create_time}\n" \
           f"Destination: {ride.destination}\n" \
           f"Arrive time: {ride.arrive_time}\n" \
           f"Total passengers: {ride.total_passengers}\n" \
           f"\n" \
           f"Best regards,\n" \
           f"RideConnect"
