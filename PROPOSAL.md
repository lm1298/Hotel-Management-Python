## Final Project Proposal
### Project Name: Hotel Management System

### Team Members:
Lakshmi Prasanna Malempati  
Sujan Varma Guntimadugu  
John Gant

### Outline of Hotel Management System Project:
#### Project Overview: 
* The hotel management project aims to create a system that manages room bookings, staff, payment, and guest information for a hotel.
* The software includes six classes that offer specific functions to manage hotel operations, 
such as adding and viewing rooms, handling guest stays, updating staff details, making payments, and booking rooms.
* The project includes six classes - Room, Guest, Staff, Payment, Booking  and Hotel.
* Hotel management software is an essential tool for modern hotels seeking to improve their operations, increase efficiency, and enhance guest experiences.

#### Project Complexity and Outcome:
* The project is of intermediate complexity and aims to create a user interactive functional hotel
management system.
* The features and functions of the project are:
  * Room management: Users can view all rooms, add a new room, and book a room.
  * Guest management: Users can add guest stays, get total stays, and get the last stay.
  * Staff management: Users can view all staff details, update staff salary, and working hours.
  * Payment management: Users can make payments and get payment details.
  * Booking management: Users can make bookings, modify bookings, cancel bookings, and get booking details.
  * Hotel management: Users can add and remove amenities.

* These features and functions help hotel management to keep track of the rooms, guests, staff, and payments easily. It also allows for efficient booking management and better customer service

* **Major Features of the Project Code**:
  * Make booking and modify booking: The program should allow the user to create a new booking and modify existing booking.
  * Add Stay and get last stay for guest: The program should allow the user to add stay for a guest and get last stay for particular guest. 
  * Add and remove Amenities: The program should allow the user to add and remove amenities for a hotel.
  * Update salary and working hours: The program should allow the user to salary and working hours for a particular staff.  

### The project includes 6 classes :
Room, Guest, Booking, Staff, Payment and Hotel.

* The Room class represents a hotel room and has the following attributes:
 
  * `room_number`: the room number
  * `room_type`: the type of the room (single, double, etc.)
  * `occupancy`: the number of people that can occupy the room
  * `price`: the price per night
  * `is_available`: a boolean flag indicating whether the room is currently available for booking.

* The Booking class represents a hotel booking and has the following attributes:
  
  * `room_number` : The unique room number of the booked room.
  * `check_in_date` : The date of check-in in the format "YYYY-MM-DD".
  *  `check_out_date` : The date of check-out in the format "YYYY-MM-DD".
  *  `num_guests` : The number of guests staying in the room.

* The Hotel class represents a hotel and has the following attributes:
  * `name` : The name of the hotel.
  * `location` : The location of the hotel.
  * `num_rooms` : The number of rooms in the hotel.
  * `stars` : The star rating of the hotel.
  * `amenities` : The amenities for the hotel.

* The Staff class represents a staff and has the following attributes:
  * `name` : the name of the staff member
  * `position` : the position of the staff member
  * `salary` : the salary of the staff member
  * `hours_worked` : the number of hours the staff member has worked

* The Guest class represents Guests information and has the following attributes:
  * `name`: The name of the guest.
  * `email`: The email address of the guest.
  * `phone_number`: The phone number of the guest.

* The Payment class represents Payment details and has the following attributes:
  * `guest` : Guest object representing the guest making the payment.
  *  `amount` (float): The amount of the payment.
  *  `is_paid` : A boolean flag indicating whether the payment has been made or not.

### Team Member Contributions:

* Lakshmi Prasanna : Responsible for developing Room, Booking Classes and conduct unit testing for both.
* Sujan Varma : Responsible for developing Guest , Hotel Classes and conduct unit testing for both.
* John Gant : Responsible for developing Staff , Payment Classes and conduct unit testing for both.


