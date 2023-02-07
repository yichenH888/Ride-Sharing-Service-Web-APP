<h1 align="center">
    DangerLog
</h1>
## Input validation

The system should handle cases where the user inputs incorrect or invalid information while creating an account, registering as a driver, or requesting a ride. This could lead to unexpected behavior or failure to perform a task.

**Solutions:** Using Django `Form` to collect users input and `Form.cleaned_data` get the valid data.

## Authentication and security

The system should handle cases where a user's login credentials are incorrect or if the user's session is compromised. This could lead to unauthorized access to sensitive information or unauthorized changes to the user's account.

**Solutions:** Using Django User and authentication.

## Ride management

The system should handle cases where the driver claims a ride but is unable to start or complete it, or if the ride requester cancels the ride. This could lead to inconsistent ride status updates and confusion for other users.

**Solutions:** As the Owner of a Ride, you can update the Ride information or cancel the Ride before it is confirmed or a Sharer joins. As a Sharer, you can modify the number of people in the Rideshare or cancel your join before the Ride is confirmed.

## Ride sharing 

The system should handle cases where a ride joiner joins a ride that has already been filled to capacity or if the ride requester changes the number of passengers after a ride has been shared. This could lead to disappointment for ride joiners and frustration for ride requesters.

**Solutions: **A driver can only confirm a Ride where the number of passengers required is less than the maximum number of passengers their registered vehicle can carry. Before the driver accepts the order, the Sharer can update the number of people joining.

## Ride Info

Bugs: The automatically generated "Create Time" does not match the time in Durham.

Solutions: The issue may be due to the server's time zone not being set to the time zone in Durham. The problem cannot be easily resolved unless the server's time zone can be changed.

## Email

Bugs: Sending multiple emails to non-existent email addresses will result in the email account being locked and unable to send further emails.

Solutions: Setting up own email server is a potential solution, however, it exceeds the requirements of this assignment.

