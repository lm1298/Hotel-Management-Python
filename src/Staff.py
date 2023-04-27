import csv


class Staff:
    """
    A class representing a staff member.

    Attributes:
    - name (str): the name of the staff member
    - position (str): the position of the staff member
    - salary (float): the salary of the staff member
    - hours_worked (float): the number of hours the staff member has worked

    Methods:
    - get_salary(): returns the salary of the staff member
    - get_staff_details(): returns a string representation of the staff member's details
    - update_salary(new_salary): updates the salary of the staff member
    - update_hours_worked(hours): updates the number of hours worked by the staff member
    """

    def __init__(self, name, position, salary, working_hours):
        self.name = name
        self.position = position
        self.salary = salary
        self.working_hours = working_hours

    def __str__(self):
        return f"{self.name} ({self.position}, ${self.salary:.2f})"

    def get_salary(self):
        """
        Returns the salary of the staff member.
        """
        return self.salary

    def get_staff_details(self):
        """
        Returns a string representation of the staff member's details.
        """
        return f"{self.name}, Position: {self.position}, Salary: ${self.salary:.2f}, Working hours: ${self.working_hours}"

    @staticmethod
    def view_all_staff_details(staff_list):
        """
        Displays the details of all staff members in a list.

        Args:
        - staff_list (list): a list of Staff objects
        """
        if not staff_list:
            print("No staff details found!")
        else:
            for staff_member in staff_list:
                print(staff_member.get_staff_details())

    def update_salary(self, name, new_salary):
        """
        Updates the salary of the staff member with the given name.

        Args:
        - name (str): the name of the staff member
        - new_salary (float): the new salary of the staff member
        """
        self.salary = new_salary
        print(f"Salary updated to {self.salary} for {self.name}")

    def update_working_hours(self, hours):
        """
        Updates the number of hours worked by the staff member.

        Args:
        - hours (float): the number of hours worked by the staff member
        """
        self.working_hours += hours
        print(f"Hours worked updated to {self.working_hours} for {self.name}")

    @classmethod
    def load_staff_details(cls, file_path):
        """
        Loads staff details from a CSV file.

        Args:
        - file_path (str): the path to the CSV file

        Returns:
        - A list of Staff objects
        """
        staff_list = []

        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            # next(reader)  # skip header row
            for row in reader:
                name = row[0]
                position = row[1]
                salary = float(row[2])
                working_hours = float(row[3])

                staff = cls(name, position, salary, working_hours)
                staff_list.append(staff)

        return staff_list


def main():
    # read staff data from CSV file
    with open('staff.csv') as file:
        reader = csv.reader(file)
        staff_data = [row for row in reader]

    # create Staff objects for each staff member
    staff_members = []
    for data in staff_data:
        staff_members.append(Staff(data[0], data[1], float(data[2]), float(data[3])))

    # get user input for staff member to update
    staff_name = input("Enter the name of the staff member to update: ")

    # find staff member in list and ask user which attribute to update
    found_staff_member = False
    for staff_member in staff_members:
        if staff_member.name == staff_name:
            found_staff_member = True
            print(staff_member.get_staff_details())
            choice = input("Enter '1' to update the salary, or '2' to update the hours worked: ")
            if choice == '1':
                new_salary = float(input("Enter the new salary for the staff member: "))
                staff_member.update_salary(staff_members,new_salary)
            elif choice == '2':
                new_hours = float(input("Enter the number of hours worked by the staff member: "))
                staff_member.update_working_hours(new_hours)
            else:
                print("Invalid choice.")
            print("Updated staff member details:")
            print(staff_member.get_staff_details())

    # print message if staff member was not found
    if not found_staff_member:
        print(f"Staff member with name {staff_name} not found.")


if __name__ == '__main__':
    main()