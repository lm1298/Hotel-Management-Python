class Guest:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.stays = []

    def add_stay(self, room):
        self.stays.append(room)

    def __str__(self):
        return f"{self.name}, Email: {self.email}, Phone: {self.phone_number}, Stays: {', '.join([str(room) for room in self.stays])}"