import csv
from datetime import datetime


class Booking:
    """
    A class to represent a booking in a hotel.

    Attributes
    ----------
    room_number : int
        The unique room number of the booked room.
    check_in_date : str
        The date of check-in in the format "YYYY-MM-DD".
    check_out_date : str
        The date of check-out in the format "YYYY-MM-DD".
    num_guests : int
        The number of guests staying in the room.

    Methods
    -------
    make_booking(room_number: int, check_in_date: str, check_out_date: str, num_guests: int) -> 'Booking':
        Create a new booking.
    modify_booking(check_in_date: str, check_out_date: str, num_guests: int) -> None:
        Modify the dates and/or number of guests for a booking.
    cancel_booking() -> None:
        Cancel a booking.
    get_bookings(filename: str) -> List['Booking']:
        Get a list of all bookings from a CSV file.
    save_booking_info(filename: str) -> None:
        Save the booking information to a CSV file.
    """

    def __init__(self, room_number: int, check_in_date: str, check_out_date: str, num_guests: int):
        """
        Initialize a new Booking object with the given attributes.

        Parameters
        ----------
        room_number : int
            The unique room number of the booked room.
        check_in_date : str
            The date of check-in in the format "YYYY-MM-DD".
        check_out_date : str
            The date of check-out in the format "YYYY-MM-DD".
        num_guests : int
            The number of guests staying in the room.
        """
        self.room_number = room_number
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.num_guests = num_guests

    @classmethod
    def make_booking(cls, room_number: int, check_in_date: str, check_out_date: str, num_guests: int) -> 'Booking':
        """
        Create a new booking.

        Parameters
        ----------
        room_number : int
            The unique room number of the booked room.
        check_in_date : str
            The date of check-in in the format "YYYY-MM-DD".
        check_out_date : str
            The date of check-out in the format "YYYY-MM-DD".
        num_guests : int
            The number of guests staying in the room.

        Returns
        -------
        Booking
            The newly created Booking object.
        """
        booking = cls(room_number, check_in_date, check_out_date, num_guests)
        return booking

    def modify_booking(self, check_in_date: str, check_out_date: str, num_guests: int) -> None:
        """
        Modify the dates and/or number of guests for a booking.

        Parameters
        ----------
        check_in_date : str
            The new date of check-in in the format "YYYY-MM-DD".
        check_out_date : str
            The new date of check-out in the format "YYYY-MM-DD".
        num_guests : int
            The new number of guests staying in the room.
        """
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.num_guests = num_guests

    def cancel_booking(self) -> None:
        """
        Cancel a booking.
        """
        self.check_in_date = None
        self.check_out_date = None
        self.num_guests = None

    @staticmethod
    def get_bookings(file_path):
        bookings = []
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    booking = Booking(int(row[0]), row[1], row[2], int(row[3]))
                    bookings.append(booking)
                except ValueError:
                    print(f"Invalid value for number of guests in row: {row}")
        return bookings

    def save_booking_info(self, filename: str) -> None:
        """
        Save the booking information to a CSV file.

        Parameters
        ----------
        filename : str
            The name of the CSV file to write to.
        """
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                self.room_number,
                self.check_in_date,
                self.check_out_date,
                self.num_guests
            ])


def main():
    bookings = Booking.get_bookings('bookings.csv')

    while True:
        print("\nHotel Booking System")
        print("--------------------")
        print("1. View all bookings")
        print("2. Add new booking")
        print("3. Modify booking")
        print("4. Cancel booking")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            if not bookings:
                print("There are no bookings to display.")
            else:
                print("Room No.   Check-in Date   Check-out Date   Guests")
                print("--------------------------------------------------")
                for booking in bookings:
                    print(
                        f"{booking.room_number:<10} {booking.check_in_date:<16} {booking.check_out_date:<17} {booking.num_guests}")

        elif choice == "2":
            room_number = int(input("Enter room number: "))
            check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
            check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
            num_guests = int(input("Enter number of guests: "))

            booking = Booking.make_booking(room_number, check_in_date, check_out_date, num_guests)
            bookings.append(booking)
            booking.save_booking_info('bookings.csv')

            print(f"Booking for room {booking.room_number} created successfully!")

        elif choice == "3":
            room_number = int(input("Enter room number to modify: "))
            booking = next((booking for booking in bookings if booking.room_number == room_number), None)

            if booking is None:
                print(f"No booking found for room {room_number}.")
            else:
                check_in_date = input("Enter new check-in date (YYYY-MM-DD): ")
                check_out_date = input("Enter new check-out date (YYYY-MM-DD): ")
                num_guests = int(input("Enter new number of guests: "))

                booking.modify_booking(check_in_date, check_out_date, num_guests)
                booking.save_booking_info('bookings.csv')

                print(f"Booking for room {booking.room_number} modified successfully!")

        elif choice == "4":
            room_number = int(input("Enter room number to cancel: "))
            booking = next((booking for booking in bookings if booking.room_number == room_number), None)

            if booking is None:
                print(f"No booking found for room {room_number}.")
            else:
                booking.cancel_booking()
                booking.save_booking_info('bookings.csv')

                print(f"Booking for room {booking.room_number} cancelled successfully!")

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == '__main__':
    main()
