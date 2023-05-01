import unittest

from src.hotel import Hotel


class TestHotel(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel("Grand India", "New York", 100, 5)

    def test_add_amenity(self):
        """
        Test that the add_amenity method adds an amenity to the hotel's list of amenities.
        """
        self.hotel.add_amenity("Pool")
        self.assertEqual(self.hotel.amenities, ["Pool"])

    def test_remove_amenity(self):
        """
        Test that the remove_amenity method removes an amenity from the hotel's list of amenities.
        """
        self.hotel.amenities = ["Pool", "Spa"]
        self.hotel.remove_amenity("Spa")
        self.assertEqual(self.hotel.amenities, ["Pool"])

    def test_get_info(self):
        """
        Test that the get_info method returns a string representation of the hotel's information.
        """
        self.hotel.amenities = ["Pool", "Spa"]
        info = self.hotel.get_info()
        expected_info = "Grand India (5 stars) in New York with 100 rooms and amenities: Pool, Spa"
        self.assertEqual(info, expected_info)

    def test_save_info(self):
        """
        Test that the save_info method saves the hotel's information to a CSV file.
        """
        self.hotel.amenities = ["Pool", "Spa"]
        filename = "test_hotel.csv"
        self.hotel.save_info(filename)
        with open(filename, 'r') as f:
            lines = f.readlines()
            expected_lines = ['Name,Location,Num Rooms,Stars,Amenities\n', 'Grand India,New York,100,5,"Pool, Spa"\n']
            self.assertEqual(lines, expected_lines)

    def test_remove_nonexistent_amenity(self):
        """
        Test that the remove_amenity method does nothing if the amenity to remove is not in the hotel's list of amenities.
        """
        self.hotel.amenities = ["Pool"]
        self.hotel.remove_amenity("Spa")
        self.assertEqual(self.hotel.amenities, ["Pool"])


if __name__ == '__main__':
    unittest.main()

