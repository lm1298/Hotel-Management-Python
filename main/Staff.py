class Staff:
    def __init__(self, name, position, salary, shift):
        self.name = name
        self.position = position
        self.salary = salary
        self.shift = shift

    def __str__(self):
        return f"{self.name} ({self.position}, ${self.salary}, {self.shift})"

    def get_salary(self):
        return self.salary

staff1 = Staff("John Doe", "Receptionist", 2500, "Shift: 8-12")
staff2 = Staff("Jane Smith", "Housekeeper", 2000, "Shift: 12-6")
staff3 = Staff("Bob Johnson", "Chef", 3500, "Shift: 6-1")

print(staff1)
print(staff2)
print(staff3)

