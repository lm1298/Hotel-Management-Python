class Staff:
    """
    Args
    - name (str): The name of the staff working
    - position (str): Position the worker is working
    - salary (int): The salary of the requested worker
    - shift (str): Shift the worker is working 
    """
    def __init__(self, name, position, salary, shift):
        self.name = name
        self.position = position
        self.salary = salary
        self.shift = shift

    def __str__(self):
        """
    Once given the required arguments above, automatically returns the workers name, position, 
    salary, and shift

    Returns: 
    - string of the workers name, position and shift they're working
    - integer of the salary they are making
    """
        return f"{self.name} ({self.position}, ${self.salary}, {self.shift})"


staff1 = Staff("John Doe", "Receptionist", 2500, "Shift: 8-12")
staff2 = Staff("Jane Smith", "Housekeeper", 2000, "Shift: 12-6")
staff3 = Staff("Bob Johnson", "Chef", 3500, "Shift: 6-1")

print(staff1)
print(staff2)
print(staff3)

