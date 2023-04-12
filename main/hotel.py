class Hotel:
    def _init_(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.rooms = []
        self.bookings = []
        self.staff = []

    def add_room(self, room):
        self.rooms.append(room)

    def remove_room(self, room):
        if room in self.rooms:
            self.rooms.remove(room)
            return True
        else:
            return False

    def find_available_rooms(self, room_type):
        available_rooms = []
        for room in self.rooms:
            if room.room_type == room_type and room.is_available():
                available_rooms.append(room)
        return available_rooms