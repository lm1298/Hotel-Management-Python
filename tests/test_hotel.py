import unittest
from datetime import date
from src.hotel import Hotel
from src.guest import Guest
from src.room import Room

class TestHotel(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel("Test Hotel", 10)

    def test_check_in(self):
        guest1 = Guest("John", "Doe")
        guest2 = Guest("Jane", "Doe")

        # Check in to available room
        self.assertTrue(self.hotel.check_in(guest1, 1, "2023-05-01", "2023-05-03"))

        # Check in to unavailable room
        self.assertFalse(self.hotel.check_in(guest2, 1, "2023-05-01", "2023-05-03"))

    def test_check_out(self):
        guest1 = Guest("John", "Doe")
        guest2 = Guest("Jane", "Doe")

        # Check out with no stays
        self.assertFalse(self.hotel.check_out(guest1))

        # Check out with stay
        self.hotel.check_in(guest1, 1, "2023-05-01", "2023-05-03")
        self.assertEqual(self.hotel.check_out(guest1), (True, 200))

    def test_get_available_rooms(self):
        room1 = Room(1, 100)
        room2 = Room(2, 200)
        self.hotel.rooms = [room1, room2]

        # No available rooms
        self.assertEqual(self.hotel.get_available_rooms("2023-05-01", "2023-05-03"), [])

        # One available room
        room1.book()
        self.assertEqual(self.hotel.get_available_rooms("2023-05-01", "2023-05-03"), [2])

        # Both rooms available
        room2.book()
        self.assertEqual(self.hotel.get_available_rooms("2023-05-01", "2023-05-03"), [])
