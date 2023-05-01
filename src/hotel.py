import csv


class Hotel:
    def __init__(self, name, location, num_rooms, stars):
        """
        Initialize a new instance of the Hotel class.
        Args:
            name (str): The name of the hotel.
            location (str): The location of the hotel.
            num_rooms (int): The number of rooms in the hotel.
            stars (int): The star rating of the hotel.
        """
        self.name = name
        self.location = location
        self.num_rooms = num_rooms
        self.stars = stars
        self.amenities = []

    def add_amenity(self, amenity):
        """Add an amenity to the hotel."""
        self.amenities.append(amenity)

    def remove_amenity(self, amenity):
        """Remove an amenity from the hotel."""
        if amenity in self.amenities:
            self.amenities.remove(amenity)
        else:
            print(f"{amenity} is not an amenity of {self.name}")

    def get_info(self):
        """Return a string representation of the hotel information."""
        return f"{self.name} ({self.stars} stars) in {self.location} with {self.num_rooms} rooms and amenities: {', '.join(self.amenities)}"

    def save_info(self, filename):
        """
           Save the hotel information to a CSV file.

           Args:
               filename (str): The name of the file to save the information to.
        """
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Location', 'Num Rooms', 'Stars', 'Amenities'])
            writer.writerow([self.name, self.location, self.num_rooms, self.stars, ', '.join(self.amenities)])
        print(f"{self.name} info saved to {filename}.")


def main():
    hotel = Hotel("Grand Hotel", "New York", 100, 5)

    print("Welcome to the hotel information system!")

    while True:
        print("\nWhat would you like to do?")
        print("1. View hotel information")
        print("2. Add an amenity")
        print("3. Remove an amenity")
        print("4. Save hotel information to file")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print(hotel.get_info())
        elif choice == "2":
            amenity = input("Enter the amenity you would like to add: ")
            hotel.add_amenity(amenity)
            print(f"{amenity} added to {hotel.name}")
        elif choice == "3":
            amenity = input("Enter the amenity you would like to remove: ")
            hotel.remove_amenity(amenity)
        elif choice == "4":
            filename = "hotel.csv"
            hotel.save_info(filename)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == '__main__':
    main()
