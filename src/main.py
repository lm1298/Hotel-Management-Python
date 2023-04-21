from datetime import date
from main.room import Room
from main.booking import Booking

# Initialize a Room object
room1 = Room(101, "Single", 1, 50)

# Initialize a Booking object
booking1 = Booking("John Smith", room1, date(2023, 5, 1), date(2023, 5, 7))


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
        checkin_date = input("Check-in date (YYYY-MM-DD): ")
        checkout_date = input("Check-out date (YYYY-MM-DD): ")
        if room1.check_availability(checkin_date, checkout_date):
            print("Room is available.")
        else:
            print("Room is not available.")
    elif choice == "2":
        guest_name = input("Guest name: ")
        checkin_date = input("Check-in date (YYYY-MM-DD): ")
        checkout_date = input("Check-out date (YYYY-MM-DD): ")
        booking = Booking(guest_name, room1, checkin_date, checkout_date)
        if booking.make_booking(guest_name, room1, checkin_date, checkout_date):
            print("Reservation made.")
        else:
            print("Room is not available.")
    elif choice == "3":
        reservations = room1.get_reservations()
        if len(reservations) == 0:
            print("There are no reservations for this room.")
        else:
            for i, reservation in enumerate(reservations):
                print(f"{i + 1}. {reservation}")
            choice = input("Enter the number of the reservation to cancel: ")
            try:
                choice = int(choice)
                reservation = reservations[choice - 1]
                room1.cancel_reservation(reservation)
            except (ValueError, IndexError):
                print("Invalid choice.")
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
        new_price = input("New price: ")
        room1.update_price(new_price)
    elif choice == "7":
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
