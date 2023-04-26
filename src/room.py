"""
A simple program to manage a hotel room reservation system.

The program loads room information from a CSV file, allows users to view all rooms, add a new room, and book a room.
The program also saves room information to the CSV file upon exiting.

Author: Prasanna

"""
import csv
from datetime import datetime


class Room:
    def __init__(self, number, capacity, price, is_booked):
        """
        Initialize a new Room object with the given attributes.

        Parameters
        ----------
        number : int
            The unique room number of the room.
        capacity : int
            number of persons in room.
        price : float
            The price of the room per night.
        is_booked : bool
            A flag indicating whether the room is currently booked or not.
        """
        self.rooms = None
        self.number = number
        self.capacity = capacity
        self.price = price
        self.is_booked = is_booked

    def book(self):
        """
            Book the room.
        """
        self.is_booked = True

    def add_room(rooms, number, capacity, price, is_booked):
        """
        Add a new room to the list of rooms.

        Args:
            rooms (list): The list of existing rooms.
            number (int): The unique room number of the new room.
            capacity (int): The maximum number of occupants for the new room.
            price (float): The price per night for the new room.

        Raises:
            ValueError: If the room number already exists in the database.
        """
        for room in rooms:
            if room.number == number:
                raise ValueError(f"Room with number {number} already exists in the database.")
        rooms.append(Room(number, capacity, price, is_booked))

    def __str__(self):
        """
            Return a string representation of the room.

            Returns:
                str: The string representation of the room.
        """
        return f"Room {self.number} (capacity: {self.capacity}, price: ${self.price}/night," \
               f" is_booked: {self.is_booked})"

    @staticmethod
    def view_all_rooms(rooms):
        """
            Display all rooms.

            Args:
                rooms (list): A list of Room objects to display.
        """
        if not rooms:
            print("No rooms found!")
        else:
            for room in rooms:
                print(room)

    @staticmethod
    def book_room(rooms, room_number, checkin_date, checkout_date):
        """
            Book a room.

            Args:
                rooms (list): A list of Room objects to search for the room.
                room_number (int): The room number to book.
                checkin_date (str): The check-in date in YYYY-MM-DD format.
                checkout_date (str): The check-out date in YYYY-MM-DD format.
        """
        for room in rooms:
            if room.number == room_number:
                if room.is_booked:
                    print(f"Room {room.number} is already booked!")
                else:
                    print(f"Booking Room {room.number} for {checkin_date} to {checkout_date}...")
                    room.book()
                    print("Room booked successfully!")
                break
        else:
            print(f"Room {room_number} not found!")

    @classmethod
    def load_from_data_file(cls, filename):
        """
            Load room information from a CSV file.

            Args:
                filename (str): The name of the CSV file.

            Returns:
                list: A list of Room objects loaded from the CSV file.
        """
        rooms = []
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    room_number = int(row[0])
                    capacity = int(row[1])
                    price = float(row[2])
                    is_booked = False if row[3].lower() == "false" else True
                    room = cls(room_number, capacity, price, is_booked)
                    rooms.append(room)
                except ValueError:
                    print(f"Invalid value for capacity for room {row[0]}")
        return rooms

    @classmethod
    def save_to_data_file(cls, rooms, filename):
        """
            Save room information to a CSV file.

            Parameters
            ----------
            rooms : list
                A list of Room objects to save.
            filename : str
                The name of the CSV file to save to.
        """

        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for room in rooms:
                writer.writerow([room.number, room.capacity, room.price, room.is_booked])


def main():
    """
        The main function that runs the hotel room reservation system.
    """
    filename = "room.csv"
    rooms = Room.load_from_data_file(filename)
    while True:
        print("\nWhat would you like to do?")
        print("1. View all rooms")
        print("2. Add a room")
        print("3. Book a room")
        print("4. Save and exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            Room.view_all_rooms(rooms)
        elif choice == "2":
            number = int(input("Enter the room number: "))
            capacity = int(input("Enter the room capacity: "))
            price = float(input("Enter the room price: "))
            is_booked = bool(input("Enter room status: "))
            try:
                Room.add_room(rooms, number, capacity, price, is_booked)
                print("Room added successfully!")
            except ValueError as error:
                print(error)
        elif choice == "3":
            number = int(input("Enter the room number: "))
            checkin_date = input("Enter the check-in date (YYYY-MM-DD): ")
            checkout_date = input("Enter the check-out date (YYYY-MM-DD): ")
            try:
                check_in = datetime.strptime(checkin_date, '%Y-%m-%d')
                check_out = datetime.strptime(checkout_date, '%Y-%m-%d')
            except ValueError:
                print("Invalid date format. Please enter dates in the format YYYY-MM-DD.")
                continue

            # Check if the check-out date is after the check-in date
            if check_out <= check_in:
                print("Check-out date must be after check-in date.")
                continue
            Room.book_room(rooms, number, checkin_date, checkout_date)
        elif choice == "4":
            Room.save_to_data_file(rooms, filename)
            print("Rooms data saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4")


if __name__ == '__main__':
    main()
