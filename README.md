<p align="center">
<a href="" rel="noopener">
    <img width=200px height=200px src="https://s2.loli.net/2023/01/28/PLAEebtz2dYcSfj.png" alt="Project logo">
</a>
</p>

<h1 align="center">
    RideConnect
</h1>

<h3>
    Duke ECE568: Engineering Robust Server Software
</h3>

> Django Web-App

Ride Sharing Service: This web-app will let users request, drive for, and join rides. 

The system allows three roles:  
- Ride Owner: A user who requests a ride 
- Driver: Provide name and vehicle information; Can claim, start, confirm and complete ride service
- Ride Sharer: Can search ride request and join the ride

Functionality supported: 

- A user should be able to create an account if they do not have one.  
- A user with an account should be able to login and logout.
- A logged-in user should be able to register as a driver and enter their personal and vehicle info. They should also be able to access and edit their info.
- If a logged-in user is part of multiple rides, she should be able to select which ride she wants to perform actions on. If a logged in user belongs to only one ride, you MAY display your ride-selecon mechanism with the one ride, or you MAY omit it (not show it). Note this should allow selectioon of any open or confirmed rides for that user (but not complete rides).
- A logged-in user should be able to request a ride. Requesting a ride should allow the owner to specify the destination address, a required arrival date / time, the number of total passengers from their party, a vehicle type (optionally), whether the ride may be shared by other users or not, and any other special requests.
- ride owner should be able to edit the specific requested attributes of the ride as long as the ride is not confirmed.
- A ride owner or sharer should be able to view the status of their non-complete rides. For open ride requests, this should show the current ride details (from the original request + any updates due to sharers joining the ride). For confirmed ride requests, the driver and vehicle details should also be shown.
- A ride driver should be able to view the status of their confirmed rides, which should show the information for the owner and each sharer of the ride, including the number of passengers in each party. A driver should also be able to edit a ride to mark it as complete.
- A driver should be able to search for open ride requests. Only requests which fit within the driver’s vehicle capacity and match the vehicle type and special request info (if either of those were specified in the ride request) should be shown. A driver can claim and start a ride service, thus confirming it. Once closed, the ride owner and each sharer should be notified by email that the ride has been confirmed (hence no further changes are allowed).
- A user should be able to search for open ride requests by specifying a destination, arrival window (the user’s earliest and latest acceptable arrival time) and number of passengers in their party. A sharer should be able to join a selected ride, if any exist in the resulting list of pending rides.
## Installation
- Django:  
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source. (Reference: https://www.djangoproject.com/)
- Docker:

```dockerfile
Lorem ipsum  
```
- Database: Postgres


## Usage example
This is the homePage of the system after registration and logging in.
![image](https://gitlab.oit.duke.edu/rs590/erss-hwk1-xl404-rs590/-/raw/master/homePage.png?inline=false)
This screenshot indicate a ride which is shared by Kelly (Ride Owner) and Hunter (Ride Sharer), the Driver is Alisa. 
![image](https://gitlab.oit.duke.edu/rs590/erss-hwk1-xl404-rs590/-/raw/master/rideDetails.png?inline=false)
This ride is requested by Kelly in "Ride Request", and can be searched in the system by all the other users with relative information in "Ride Search". Hunter jolisa becomes the drivined the ride to become a ride sharer. As a driver who provided personal information and vehicle information in "Driver", Aer. All of this three users can find their ride in the "My Rides" Section. All the user can check and edit their personal information in "Profile".




