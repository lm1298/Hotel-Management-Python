import unittest

from src.room import Room


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room(101, 2, 100.0, False)
        self.room2 = Room(102, 4, 200.0, True)
        self.room3 = Room(103, 6, 300.0, False)
        self.rooms = [self.room1, self.room2, self.room3]

    def test_room_init(self):
        self.assertEqual(self.room1.number, 101)
        self.assertEqual(self.room1.capacity, 2)
        self.assertEqual(self.room1.price, 100.0)
        self.assertFalse(self.room1.is_booked)

    def test_room_str(self):
        expected_output = "Room 101 (capacity: 2, price: $100.0/night)"
        self.assertEqual(str(self.room1), expected_output)

    def test_load_from_data_file(self):
        rooms = Room.load_from_data_file("test_rooms.csv")
        self.assertEqual(len(rooms), 3)
        self.assertEqual(rooms[0].number, 101)
        self.assertEqual(rooms[1].capacity, 4)
        self.assertAlmostEqual(rooms[2].price, 300.0, delta=0.01)
        self.assertFalse(rooms[0].is_booked)
        self.assertTrue(rooms[1].is_booked)

    def test_view_all_rooms(self):
        expected_output = "Room 101 (capacity: 2, price: $100.0/night)\nRoom 102 (capacity: 4, price: $200.0/night)\nRoom 103 (capacity: 6, price: $300.0/night)\n"
        self.assertEqual(expected_output, capture_stdout(Room.view_all_rooms, self.rooms))

    def test_book_room(self):
        Room.book_room(self.rooms, 101, "2023-05-01", "2023-05-05")
        self.assertTrue(self.room1.is_booked)
        Room.book_room(self.rooms, 102, "2023-05-01", "2023-05-05")
        self.assertTrue(self.room2.is_booked)

    def test_save_to_data_file(self):
        Room.save_to_data_file(self.rooms, "test_rooms.csv")
        rooms = Room.load_from_data_file("test_rooms.csv")
        self.assertEqual(len(rooms), 3)
        self.assertEqual(rooms[0].number, 101)
        self.assertEqual(rooms[1].capacity, 4)
        self.assertAlmostEqual(rooms[2].price, 300.0, delta=0.01)
        self.assertFalse(rooms[0].is_booked)
        self.assertTrue(rooms[1].is_booked)


def capture_stdout(function, *args, **kwargs):
    from io import StringIO
    import sys

    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    function(*args, **kwargs)

    sys.stdout = old_stdout
    return mystdout.getvalue()


if __name__ == '__main__':
    unittest.main()
