import unittest
from datetime import datetime

from src.room import Room


class TestRoomMethods(unittest.TestCase):
    def setUp(self):
        self.room1 = Room(101, 2, 75.0, False)
        self.room2 = Room(102, 3, 100.0, True)
        self.rooms = [self.room1, self.room2]
        self.filename = "test_rooms.csv"
        Room.save_to_data_file(self.rooms, 'test_rooms.csv')

    def test_book(self):
        self.room1.book()
        self.assertTrue(self.room1.is_booked)

    def test_add_room(self):
        with self.assertRaises(ValueError):
            Room.add_room(self.rooms, 101, 2, 75.0, False)
        Room.add_room(self.rooms, 103, 2, 80.0, False)
        self.assertEqual(len(self.rooms), 3)

    def test_book_room(self):
        checkin_date = datetime(2023, 5, 1)
        checkout_date = datetime(2023, 5, 5)
        Room.book_room(self.rooms, 102, checkin_date, checkout_date)
        self.assertTrue(self.room2.is_booked)

    def test_load_from_data_file(self):
        rooms = Room.load_from_data_file(self.filename)
        self.assertEqual(len(rooms), 2)
        self.assertEqual(rooms[0].number, self.room1.number)
        self.assertEqual(rooms[0].capacity, self.room1.capacity)
        self.assertEqual(rooms[0].price, self.room1.price)
        self.assertEqual(rooms[0].is_booked, self.room1.is_booked)

    def test_save_to_data_file(self):
        room3 = Room(103, 2, 80.0, False)
        self.rooms.append(room3)
        Room.save_to_data_file(self.rooms, 'test_rooms.csv')
        rooms = Room.load_from_data_file('test_rooms.csv')
        self.assertEqual(len(rooms), 3)
        self.assertEqual(rooms[-1].number, room3.number)
        self.assertEqual(rooms[-1].capacity, room3.capacity)
        self.assertEqual(rooms[-1].price, room3.price)
        self.assertEqual(rooms[-1].is_booked, room3.is_booked)


if __name__ == '__main__':
    unittest.main()
