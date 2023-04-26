import unittest
from src.guest import Guest
from src.room import Room


class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("John Doe", "johndoe@example.com", "123-456-7890")

    def test_add_stay(self):
        """
        Test that a stay is added to the guest's record correctly.
        """
        self.guest.add_stay(self.room)
        self.assertEqual(self.guest.get_total_stays(), 1)

    def test_get_last_stay(self):
        """
        Test that the last stay of the guest is retrieved correctly.
        """
        self.guest.add_stay(self.room)
        self.assertEqual(self.guest.get_last_stay(), self.room)

    def test_to_csv(self):
        """
        Test that the guest's information is saved to a CSV file correctly.
        """
        self.guest.to_csv("test_guest.csv")
        # Assert that the file was created
        with open("test_guest.csv") as f:
            self.assertIsNotNone(f.read())