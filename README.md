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

This web application provides a platform for users to request rides, offer rides, and join existing rides as passengers.     

## Features

The system is designed to accommodate three user roles:  
- Ride Requester: A user who initiates a ride request.
- Driver: A user who provides their name and vehicle information, and has the ability to claim, start, confirm, and complete rides.  
- Ride Joiner: A user who searches for available rides and joins them as a passenger.  

Functionality supported: 

- Account creation and login for users
- Driver registration and information management
  - Option to register as a driver
  - Ability to enter and manage personal and vehicle information
- Ride request
  - Specify destination address, arrival date/time, number of passengers, vehicle type, whether ride may be shared, and special requests
  - Ability for ride owner to edit ride details before confirmation
- Ride status and management
  - View status of non-complete rides for owners and sharers
    - Open rides display current details including updates from sharers
    - Confirmed rides display driver and vehicle information
  - View status of confirmed rides for drivers
    - Display information for owners and sharers including passenger count
  - Ability for drivers to mark rides as complete
  - Search for open ride requests for drivers
    - Claim and confirm rides
  - Search for open ride requests for users by destination, arrival window, and passenger count
  - Ability for sharers to join selected rides from search results
## Installation
- Docker:

```dockerfile
sudo docker-compose up
```

## Usage example
Upon successful registration and login, users are presented with the home page, where they can access various features and functionalities of the ride sharing service.
![image](https://gitlab.oit.duke.edu/rs590/erss-hwk1-xl404-rs590/-/raw/master/homePage.png?inline=false)
The screenshot shows a confirmed ride with Kelly as the Ride Owner and Hunter as the Ride Sharer. Alisa, who has registered as a driver, is the driver for this ride. The details of the ride, including the driver and vehicle information, can be viewed in this section.
![image](https://gitlab.oit.duke.edu/rs590/erss-hwk1-xl404-rs590/-/raw/master/rideDetails.png?inline=false)
This ride was requested by Kelly in the "Ride Request" section, marked as shareable and thus became available for other users to search for in the "Ride Search" area. Hunter joined the ride as a ride sharer. Alisa, as a driver who previously entered their personal and vehicle information in the "Driver" section, became the driver for this ride. All three users, Kelly, Hunter and Alisa, can access details of this ride under the "My Rides" section. All users can also view and make changes to their personal information in their "Profile."



