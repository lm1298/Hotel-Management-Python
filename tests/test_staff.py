import unittest
from src.Staff import Staff

class TestStaff(unittest.TestCase):

    def test_init(self):
        # Test creating Staff objects using the CSV data
        staff1 = Staff("John Doe", "Receptionist", 2500, "Shift: 8-12")
        self.assertEqual(staff1.name, "John Doe")
        self.assertEqual(staff1.position, "Receptionist")
        self.assertEqual(staff1.salary, 2500)
        self.assertEqual(staff1.shift, "Shift: 8-12")

        staff2 = Staff("Jane Smith", "Housekeeper", 2000, "Shift: 12-6")
        self.assertEqual(staff2.name, "Jane Smith")
        self.assertEqual(staff2.position, "Housekeeper")
        self.assertEqual(staff2.salary, 2000)
        self.assertEqual(staff2.shift, "Shift: 12-6")

        staff3 = Staff("Bob Johnson", "Chef", 3500, "Shift: 6-1")
        self.assertEqual(staff3.name, "Bob Johnson")
        self.assertEqual(staff3.position, "Chef")
        self.assertEqual(staff3.salary, 3500)
        self.assertEqual(staff3.shift, "Shift: 6-1")

    def test_str(self):
        # Test the string representation of Staff objects
        staff1 = Staff("John Doe", "Receptionist", 2500, "Shift: 8-12")
        self.assertEqual(str(staff1), "John Doe (Receptionist, $2500, Shift: 8-12)")

        staff2 = Staff("Jane Smith", "Housekeeper", 2000, "Shift: 12-6")
        self.assertEqual(str(staff2), "Jane Smith (Housekeeper, $2000, Shift: 12-6)")

        staff3 = Staff("Bob Johnson", "Chef", 3500, "Shift: 6-1")
        self.assertEqual(str(staff3), "Bob Johnson (Chef, $3500, Shift: 6-1)")

if __name__ == '__main__':
    unittest.main()