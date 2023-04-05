class Room:
    """
    create a Room information for hotel management project.
    """

    def __init__(self, room_number, room_type, occupancy, price):
        self.room_number = room_number
        self.room_type = room_type
        self.occupancy = occupancy
        self.price = price
        self.reservations = []



    def check_availability(self, checkin_date, checkout_date):
        # Iterate through each reservation for this room
        for reservation in self.reservations:
            # If the reservation overlaps with the specified dates, the room is not available
            if (checkin_date < reservation.checkout_date) and (checkout_date > reservation.checkin_date):
                return False
        # If no reservations overlap with the specified dates, the room is available
        return True

    def book_room(self):
        """book room method."""
        if not self.check_availability:
            print(f"Room {self.room_number} has been booked.")
        else:
            print(f"Room {self.room_number} is not available.")

    def __str__(self):
        """ string representation of room information"""
        return f"Room {self.room_number}, Type: {self.room_type}," \
               f" Occupancy: {self.occupancy}, Price: {self.price},"