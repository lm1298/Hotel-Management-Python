import csv

class Staff:
    """
    A class representing a staff member.

    Attributes:
    name (str): The name of the staff member.
    position (str): The position of the staff member.
    salary (int): The salary of the staff member.
    shift (str): The shift of the staff member.
    """
    def __init__(self, name, position, salary, shift):
        """
    Initialize a new instance of the Staff class.

    Args:
    name (str): The name of the staff member.
    position (str): The position of the staff member.
    salary (int): The salary of the staff member.
    shift (str): The shift of the staff member.
    """
        self.name = name
        self.position = position
        self.salary = salary
        self.shift = shift

    def __str__(self):
        """
     Return a string representation of the Staff instance.
     """
        return f"{self.name} ({self.position}, ${self.salary}, {self.shift})"
    """
    Create an empty list to store staff details
    """
staff_list = []
"""
    Read the CSV file and store staff details in the list
    """
with open('staff.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip the header row
    for row in reader:
        name = row[0]
        position = row[1]
        salary = int(row[2])
        shift = row[3]
        staff = Staff(name, position, salary, shift)
        staff_list.append(staff)
"""
Print the details of each staff member
"""
for staff in staff_list:
    print(staff)
