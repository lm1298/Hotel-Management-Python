import unittest
from datetime import datetime

from yapftests.main_test import captured_output

from src.room import Room


class RoomTests(unittest.TestCase):

    def setUp(self):
        self.room1 = Room(101, 2, 50.0, False)
        self.room2 = Room(102, 4, 100.0, True)
        self.rooms = [self.room1, self.room2]

    def test_add_room(self):
        # Test adding a new room to the list of rooms
        Room.add_room(self.rooms, 103, 3, 75.0, False)
        self.assertEqual(len(self.rooms), 3)
        self.assertEqual(self.rooms[2].number, 103)
        self.assertEqual(self.rooms[2].capacity, 3)
        self.assertEqual(self.rooms[2].price, 75.0)
        self.assertEqual(self.rooms[2].is_booked, False)

        # Test adding a room with an existing room number
        with self.assertRaises(ValueError):
            Room.add_room(self.rooms, 101, 2, 50.0, False)

    def test_book_room(self):
        # Test booking an available room
        Room.book_room(self.rooms, 101, '2023, 4, 26', '2023, 4, 27')
        self.assertTrue(self.room1.is_booked)

        # Test booking a room that is already booked
        expected_output = "Room 102 is already booked!\n"
        with captured_output() as (out, err):
            Room.book_room(self.rooms, 102, '2023, 4, 26', '2023, 4, 27')
        self.assertEqual(out.getvalue(), expected_output)

        # Test booking a room that doesn't exist
        expected_output = "Room 103 not found!\n"
        with captured_output() as (out, err):
            Room.book_room(self.rooms, 103, '2023, 4, 26', '2023, 4, 27')
        self.assertEqual(out.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
