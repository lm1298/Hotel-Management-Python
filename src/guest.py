class Guest:
    """
    A class representing a hotel guest.
    """
    def __init__(self, name: str, email: str, phone_number: str):
        """
        Initializes a Guest instance.

        :param name: The name of the guest.
        :param email: The email address of the guest.
        :param phone_number: The phone number of the guest.
        """
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.stays = []

    def add_stay(self, room):
        """
        Adds a stay for the guest.

        :param room: The room that the guest stayed in.
        """
        self.stays.append(room)

    def get_total_stays(self) -> int:
        """
        Returns the total number of stays for the guest.

        :return: The total number of stays for the guest.
        """
        return len(self.stays)

    def get_last_stay(self):
        """
        Returns the last room that the guest stayed in, or None if the guest has never stayed in a room.

        :return: The last room that the guest stayed in, or None if the guest has never stayed in a room.
        """
        if len(self.stays) > 0:
            return self.stays[-1]
        else:
            return None

    def __str__(self) -> str:
        """
        Returns a string representation of the guest.

        :return: A string representation of the guest.
        """
        return f"{self.name}, Email: {self.email}, Phone: {self.phone_number}, Stays: {', '.join([str(room) for room in self.stays])}"
