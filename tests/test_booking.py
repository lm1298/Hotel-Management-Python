import datetime
import unittest

from main.room import Room


class TestBooking(unittest.TestCase):
    def setUp(self):
        self.room = "data/room.csv"
        self.booking = Booking('John Doe', self.room, datetime.date(2023, 4, 20), datetime.date(2023, 4, 22))

    def test_get_total_price(self):
        self.assertEqual(self.booking.get_total_price(), 200)

    def test_make_booking(self):
        room2 = Room(2, 'double', 1, 150)
        new_booking = self.booking.make_booking('Jane Doe', room2,
                                                datetime.date(2023, 4, 23), datetime.date(2023, 4, 25))
        self.assertIsNotNone(new_booking)
        self.assertIn(new_booking, self.booking.bookings)
        self.assertFalse(room2.is_available())

        # Attempt to book the same room again for overlapping dates
        overlapping_booking = self.booking.make_booking('Joe Bloggs', self.room,
                                                        datetime.date(2023, 4, 21), datetime.date(2023, 4, 23))
        self.assertIsNone(overlapping_booking)
        self.assertEqual(len(self.booking.bookings), 1)

    def test_modify_booking(self):
        new_price = self.booking.modify_booking(self.booking,
                                                datetime.date(2023, 4, 21), datetime.date(2023, 4, 23))
        self.assertEqual(self.booking.checkin_date, datetime.date(2023, 4, 21))
        self.assertEqual(self.booking.checkout_date, datetime.date(2023, 4, 23))
        self.assertEqual(new_price, 200)

        # Attempt to modify booking with overlapping dates
        overlapping_booking = self.booking.modify_booking(self.booking, datetime.date(2023, 4, 19),
                                                          datetime.date(2023, 4, 21))
        self.assertIsNone(overlapping_booking)
        self.assertEqual(self.booking.checkin_date, datetime.date(2023, 4, 21))
        self.assertEqual(self.booking.checkout_date, datetime.date(2023, 4, 23))

    def test_get_occupancy_rate(self):
        self.assertEqual(self.booking.get_occupancy_rate(), 0.0)

        # Make a new booking for the same room and check occupancy rate again
        room2 = Room(5, 'double', 2, 150)
        self.booking.make_booking('Jane Doe', room2, datetime.date(2023, 4, 23), datetime.date(2023, 4, 25))
        self.assertEqual(self.booking.get_occupancy_rate(), 0.5)


if __name__ == '__main__':
    unittest.main()
