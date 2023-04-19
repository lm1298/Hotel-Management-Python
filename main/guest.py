class Guest:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.stays = []

    def add_stay(self, room):
        self.stays.append(room)

    def get_total_stays(self):
        return len(self.stays)

    def get_last_stay(self):
        if len(self.stays) > 0:
            return self.stays[-1]
        else:
            return None

    def __str__(self):
        return f"{self.name}, Email: {self.email}, Phone: {self.phone_number}, Stays: {', '.join([str(room) for room in self.stays])}"