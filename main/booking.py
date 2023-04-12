class Booking:
    def __init__(self, guest, room, checkin_date, checkout_date):
        self.guest = guest
        self.room = room
        self.bookings = []
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date

    def get_occupancy_rate(self):
        total_rooms = len(self.room.rooms)
        occupied_rooms = 0
        for room in self.room.rooms:
            if not room.is_available():
                occupied_rooms += 1
        return occupied_rooms / total_rooms

    def modify_booking(self, booking, new_checkin_date, new_checkout_date):
        if booking.room.is_available(new_checkin_date, new_checkout_date):
            booking.checkin_date = new_checkin_date
            booking.checkout_date = new_checkout_date
            nights = (booking.checkout_date - booking.checkin_date).days
            booking.room.cancel_booking()
            booking.room.book()
            return nights * booking.room.price
        else:
            return None

    def get_total_price(self):
        nights = (self.checkout_date - self.checkin_date).days
        return self.room.price * nights

    def make_booking(self, guest, room, checkin_date, checkout_date):
        if room.is_available():
            booking = Booking(guest, room, checkin_date, checkout_date)
            self.bookings.append(booking)
            room.book()
            return booking
        else:
            return None

    def __str__(self):
        return f"{self.guest} booked {self.room} from {self.checkin_date} to {self.checkout_date}"
