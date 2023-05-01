
import csv
import os

from src.room import Room


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

    def add_stay(self, room, checkin, checkout):
        """
        Adds a stay for the guest.

        :param room: The room that the guest stayed in.
        :param checkin: The check-in date for the stay.
        :param checkout: The check-out date for the stay.
        """
        self.stays.append((room, checkin, checkout))

    def get_total_stays(self) -> int:
        """
        Returns the total number of stays for the guest.

        :return: The total number of stays for the guest.
        """
        return len(self.stays)

    def get_last_stay(self):
        """
        Returns the last room that the guest stayed in, or None if the guest has never stayed in a room.

        :return: A string representation of the last room that the guest stayed in, or None if the guest has never stayed in a room.
        """
        if len(self.stays) > 0:
            room, checkin, checkout = self.stays[-1]
            return f"Room {room.number}: {room}, Check-in: {checkin}, Check-out: {checkout}"
        else:
            return None

    def __str__(self) -> str:
        """
        Returns a string representation of the guest.

        :return: A string representation of the guest.
        """
        return f"{self.name}, Email: {self.email}, Phone: {self.phone_number}"

    def to_csv(self, filename: str):
        """
        Writes the guest information to a CSV file.

        :param filename: The name of the file to write to.
        """
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.name, self.email, self.phone_number])


def main():
    print("Welcome to the Hotel Management System!")
    name = input("Please enter your name: ")
    email = input("Please enter your email: ")
    phone_number = input("Please enter your phone number: ")
    guest = Guest(name, email, phone_number)

    while True:
        print("\nPlease select an option:")
        print("1. Add a stay")
        print("2. Get the total number of stays")
        print("3. Get the last stay")
        print("4. Write guest information to a CSV file")
        print("5. Quit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            number = int(input("Enter the room number: "))
            capacity = int(input("Enter the room capacity: "))
            price = float(input("Enter the room price: "))
            is_booked = bool(input("Enter room status: "))
            checkin = input("Please enter the check-in date (YYYY-MM-DD): ")
            checkout = input("Please enter the check-out date (YYYY-MM-DD): ")
            room = Room(number, capacity, price, is_booked)
            guest.add_stay(room, checkin, checkout)
            print("Stay added!")

        elif choice == "2":
            print(f"Total number of stays: {guest.get_total_stays()}")

        elif choice == "3":
            last_stay = guest.get_last_stay()
            if last_stay:
                print(f"Last stay: {last_stay}")
            else:
                print("No stays found for this guest.")

        elif choice == "4":
            filename = input("Please enter the filename to write to: ")
            guest.to_csv(filename)
            print("Guest information written to CSV file.")

        elif choice == "5":
            print("Thank you for using the Hotel Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()

