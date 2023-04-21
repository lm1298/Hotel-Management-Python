from datetime import datetime
from src.room import Room
from src.booking import Booking

# Initialize a Room object
room1 = Room(101, "Single", 1, 50)
room2 = Room(102, 'single', 2, 100)
# Initialize a Booking object
booking1 = Booking("prasanna", room1, "2023-09-08", "2023-09-11")


# Define a function to display the menu
def display_menu():
    print("1. Check room availability")
    print("2. Make a reservation")
    print("3. Cancel a reservation")
    print("4. View reservations")
    print("5. Get room revenue")
    print("6. Update room price")
    print("7. Update room occupancy")
    print("8. Exit")


# Define a function to handle user input and execute commands
def handle_input(choice):
    if choice == "1":
        while True:
            checkin_date = input("Check-in date (YYYY-MM-DD): ")
            checkout_date = input("Check-out date (YYYY-MM-DD): ")
            try:
                datetime.strptime(checkin_date, '%Y-%m-%d')
                datetime.strptime(checkout_date, '%Y-%m-%d')
            except ValueError:
                print("Invalid date format. Please try again.")
                continue
            if datetime.strptime(checkin_date, '%Y-%m-%d') >= datetime.strptime(checkout_date,
                                                                                '%Y-%m-%d'):
                print("Check-out date must be after check-in date. Please try again.")
                continue
            if room1.check_availability(checkin_date, checkout_date):
                print("Room is available.")
            else:
                print("Room is not available.")
            break
    elif choice == "2":
        while True:
            guest_name = input("Guest name: ")
            room = input("enter room number:")
            checkin_date = input("Check-in date (YYYY-MM-DD): ")
            checkout_date = input("Check-out date (YYYY-MM-DD): ")
            try:
                datetime.strptime(checkin_date, '%Y-%m-%d')
                datetime.strptime(checkout_date, '%Y-%m-%d')
            except ValueError:
                print("Invalid date format. Please try again.")
                continue
            if datetime.strptime(checkin_date, '%Y-%m-%d') >= datetime.strptime(checkout_date,
                                                                                      '%Y-%m-%d'):
                print("Check-out date must be after check-in date. Please try again.")
                continue
            #booking = Booking(guest_name, room, checkin_date, checkout_date)
            if room1.book_room():
                print("Reservation made.")
            else:
                print("Room is not available.")
            break
    elif choice == "3":
        reservations = room1.get_reservations()
        if len(reservations) == 0:
            print("There are no reservations for this room.")
        else:
            while True:
                for i, reservation in enumerate(reservations):
                    print(f"{i + 1}. {reservation}")
                choice = input("Enter the number of the reservation to cancel: ")
                try:
                    choice = int(choice)
                    if choice < 1 or choice > len(reservations):
                        raise ValueError
                    reservation = reservations[choice - 1]
                    room1.cancel_reservation(reservation)
                    print("Reservation cancelled.")
                    break
                except (ValueError, IndexError):
                    print("Invalid choice. Please try again.")
                    continue
    elif choice == "4":
        reservations = room1.get_reservations()
        if len(reservations) == 0:
            print("There are no reservations for this room.")
        else:
            for reservation in reservations:
                print(reservation)
    elif choice == "5":
        revenue = room1.get_revenue()
        print(f"Total revenue for this room: ${revenue}")
    elif choice == "6":
        while True:
            new_price = input("New price: ")
            try:
                new_price = float(new_price)
            except ValueError:
                print("Invalid price format. Please try again.")
                continue
            if new_price <= 0:
                print("Price must be greater than 0. Please try again.")
                continue
            room1.update_price(new_price)
            print("Price updated.")
            break
    elif choice == "7":
        while True:
            new_occupancy = input("New occupancy: ")
            room1.update_occupancy(new_occupancy)
    elif choice == "8":
        exit()
    else:
        print("Invalid choice.")


# Display the menu and handle user input
while True:
    display_menu()
    choice = input("Enter your choice: ")
    handle_input(choice)
