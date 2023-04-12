class Staff:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.name} ({self.position}, ${self.salary})"

    def get_salary(self):
        return self.salary

staff1 = Staff("John Doe", "Receptionist", 2500)
staff2 = Staff("Jane Smith", "Housekeeper", 2000)
staff3 = Staff("Bob Johnson", "Chef", 3500)

print(staff1)
print(staff2)
print(staff3)