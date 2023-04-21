class Booking:
    """A class representing a booking made by a guest for a room at a hotel."""

    def __init__(self, guest, rooms, checkin_date, checkout_date):
        """
        Initialize a new Booking object.

        Args:
        - guest (str): The name of the guest making the booking.
        - room (Room): The room being booked.
        - checkin_date (date): The date the guest will check in.
        - checkout_date (date): The date the guest will check out.
        """
        self.guest = guest
        self.room = rooms
        self.bookings = []
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date
        self.is_available = None

    def get_occupancy_rate(self):
        """Returns the occupancy rate of the hotel."""
        total_rooms = len(self.room.rooms)
        occupied_rooms = 0
        for room in self.room.rooms:
            if not room.is_available():
                occupied_rooms += 1
        return occupied_rooms / total_rooms

    def get_total_price(self):
        """
        Calculate the total price of the booking.

        Returns:
        - float: The total price of the booking.
        """
        nights = (self.checkout_date - self.checkin_date).days
        return self.room.price * nights

    def make_booking(self, guest, room, checkin_date, checkout_date):
        """
        Make a new booking and add it to the list of bookings for this object.

        Args:
        - guest (str): The name of the guest making the booking.
        - room (Room): The room being booked.
        - checkin_date (date): The date the guest will check in.
        - checkout_date (date): The date the guest will check out.

        Returns:
        - Booking: The newly created Booking object.
        - None: If the room is not available.
        """
        if room.is_available():
            booking = Booking(guest, room, checkin_date, checkout_date)
            self.bookings.append(booking)
            room.book()
            return booking
        else:
            return None

    def modify_booking(self, new_checkin_date, new_checkout_date):
        """
        Modifies an existing booking with new check-in and check-out dates.
    
                Args:
                    self (Booking): An instance of the Booking class representing the booking to be modified.
                    new_checkin_date (datetime.date): The new check-in date for the booking.
                    new_checkout_date (datetime.date): The new check-out date for the booking.
    
                Returns:
                    float: The cost of the modified booking.
    
                    None: If the room is not available for the new dates.
    
        """
        if self.room.is_available(new_checkin_date, new_checkout_date):
            self.checkin_date = new_checkin_date
            self.checkout_date = new_checkout_date
            nights = (self.checkout_date - self.checkin_date).days
            self.room.cancel_booking()
            self.room.book()
            return nights * self.room.price
        else:
            return

    def __str__(self):
        """Returns a string representation of the booking."""
        return f"{self.guest} booked {self.room} from {self.checkin_date} to {self.checkout_date}"
