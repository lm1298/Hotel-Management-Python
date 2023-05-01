import os
import unittest
from src.guest import Guest
from src.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("John Smith", "johnsmith@example.com", "555-1234")
        self.room = Room(101, 2, 100.0, False)

    def test_add_stay(self):
        self.guest.add_stay(self.room, "2023-05-01", "2023-05-05")
        self.assertEqual(len(self.guest.stays), 1)
        self.assertEqual(self.guest.stays[0][0], self.room)
        self.assertEqual(self.guest.stays[0][1], "2023-05-01")
        self.assertEqual(self.guest.stays[0][2], "2023-05-05")

    def test_get_total_stays(self):
        self.assertEqual(self.guest.get_total_stays(), 0)
        self.guest.add_stay(self.room, "2023-05-01", "2023-05-05")
        self.assertEqual(self.guest.get_total_stays(), 1)

    def test_get_last_stay(self):
        self.assertIsNone(self.guest.get_last_stay())
        self.guest.add_stay(Room(102, 2, 120.0, False), "2023-04-20", "2023-04-25")
        self.guest.add_stay(Room(103, 3, 150.0, False), "2023-05-10", "2023-05-12")
        last_stay = self.guest.get_last_stay()
        self.assertIsNotNone(last_stay)
        self.assertIn("Room 103", last_stay)

    def test_to_csv(self):
        # Clear previous content in file
        filename = "test_guest.csv"
        with open(filename, mode="w", newline="") as file:
            file.write("")
        self.guest.to_csv(filename)

        # Check if file exists and has correct content
        file_exists = os.path.isfile(filename)
        with open(filename) as file:
            lines = file.readlines()
        self.assertEqual(len(lines), 1)
        self.assertEqual(lines[0].strip(), "John Smith,johnsmith@example.com,555-1234")


if __name__ == '__main__':
    unittest.main()

