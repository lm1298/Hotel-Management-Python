class Hotel:
    """
    A class to represent a hotel.

    Attributes
    ----------
    name : str
        The name of the hotel.
    address : str
        The address of the hotel.
    phone_number : str
        The phone number of the hotel.
    rooms : list
        A list of Room objects representing the rooms in the hotel.
    bookings : list
        A list of Booking objects representing the bookings made in the hotel.
    staff : list
        A list of Staff objects representing the staff members in the hotel.
    """

    def __init__(self, name, address, phone_number):
        """
        Constructs all the necessary attributes for the hotel object.

        Parameters
        ----------
        name : str
            The name of the hotel.
        address : str
            The address of the hotel.
        phone_number : str
            The phone number of the hotel.
        """
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.rooms = []
        self.bookings = []
        self.staff = []

    def add_room(self, room):
        """
        Add a room to the list of rooms in the hotel.

        Parameters
        ----------
        room : Room
            A Room object representing the room to be added.

        Returns
        -------
        bool
            True if the room was added successfully, False otherwise.
        """
        self.rooms.append(room)

    def remove_room(self, room):
        """
        Remove a room from the list of rooms in the hotel.

        Parameters
        ----------
        room : Room
            A Room object representing the room to be removed.

        Returns
        -------
        bool
            True if the room was removed successfully, False otherwise.
        """
        if room in self.rooms:
            self.rooms.remove(room)
            return True
        else:
            return False

    def find_available_rooms(self, room_type):
        """
        Find all available rooms of a given room type.

        Parameters
        ----------
        room_type : str
            A string representing the room type.

        Returns
        -------
        list
            A list of Room objects representing the available rooms of the given room type.
        """
        available_rooms = []
        for room in self.rooms:
            if room.room_type == room_type and room.is_available():
                available_rooms.append(room)
        return available_rooms

    def get_bookings_for_room(self, room_number):
        """
        Get all bookings made for a given room.

        Parameters
        ----------
        room_number : str
            A string representing the room number.

        Returns
        -------
        list
            A list of Booking objects representing the bookings made for the given room.
        """
        bookings = []
        for booking in self.bookings:
            if booking.room.number == room_number:
                bookings.append(booking)
        return bookings
