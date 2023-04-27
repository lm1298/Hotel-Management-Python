import csv
from datetime import datetime
import unittest

from src.booking import Booking


class TestBooking(unittest.TestCase):
    """A test suite for the Booking class"""

    def setUp(self):
        """Sets up the test suite by creating a list of bookings from a CSV file"""
        self.bookings = []
        with open('test_bookings.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                room_number = int(row[0])
                check_in_date = datetime.strptime(row[1], '%Y-%m-%d')
                check_out_date = datetime.strptime(row[2], '%Y-%m-%d')
                num_guests = int(row[3])
                booking = Booking.make_booking(room_number, check_in_date, check_out_date, num_guests)
                self.bookings.append(booking)

    def test_make_booking(self):
        """Tests the make_booking method of the Booking class"""
        booking = self.bookings[0]
        self.assertEqual(booking.room_number, 101)
        self.assertEqual(booking.check_in_date, datetime(2023, 5, 1))
        self.assertEqual(booking.check_out_date, datetime(2023, 5, 3))
        self.assertEqual(booking.num_guests, 2)

    def test_modify_booking(self):
        """Tests the modify_booking method of the Booking class"""
        booking = self.bookings[0]
        booking.modify_booking(datetime(2023, 5, 2), datetime(2023, 5, 4), 3)
        self.assertEqual(booking.check_in_date, datetime(2023, 5, 2))
        self.assertEqual(booking.check_out_date, datetime(2023, 5, 4))
        self.assertEqual(booking.num_guests, 3)

    def test_cancel_booking(self):
        """Tests the cancel_booking method of the Booking class"""
        booking = self.bookings[0]
        booking.cancel_booking()
        self.assertIsNone(booking.check_in_date)
        self.assertIsNone(booking.check_out_date)
        self.assertIsNone(booking.num_guests)


if __name__ == '__main__':
    unittest.main()
