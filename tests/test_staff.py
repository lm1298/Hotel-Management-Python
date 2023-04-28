import csv
import unittest

from src.Staff import Staff


class TestStaff(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load staff details from test_staff.csv
        cls.staff_list = Staff.load_staff_details('test_staff.csv')

    def test_get_salary(self):
        """
        Test the `get_salary` method of the `Staff` class.

        Checks that the method returns the expected salary for a staff member.
        """
        staff_member = self.staff_list[0]
        expected_salary = 300.5
        self.assertEqual(staff_member.get_salary(), expected_salary)

    def test_update_salary(self):
        """
        Test the `update_salary` method of the `Staff` class.

        Checks that the method updates the salary of a staff member correctly.
        """
        staff_member = self.staff_list[0]
        new_salary = 600
        staff_member.update_salary(staff_member.name, new_salary)
        self.assertEqual(staff_member.get_salary(), new_salary)

    def test_update_working_hours(self):
        """
        Test the `update_working_hours` method of the `Staff` class.

        Checks that the method updates the working hours of a staff member correctly.
        """
        staff_member = self.staff_list[0]
        old_hours = staff_member.working_hours
        additional_hours = 10.0
        staff_member.update_working_hours(additional_hours)
        self.assertEqual(staff_member.working_hours, old_hours + additional_hours)


if __name__ == '__main__':
    # Run tests
    unittest.main()