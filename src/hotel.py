from typing import List, Tuple

from src.guest import Guest
from src.room import Room


class Hotel:
    """
    A class representing a hotel with rooms and guests.
    """

    def _init_(self, name: str, num_rooms: int):
        """
        Initializes a Hotel instance.

        :param name: The name of the hotel.
        :param num_rooms: The number of rooms in the hotel.
        """
        self.name = name
        self.num_rooms = num_rooms
        self.rooms = []
        self.guests = []

    def check_in(self, guest: Guest, room_number: int, check_in_date: str, check_out_date: str) -> bool:
        """
        Checks a guest into a room if the room is available.

        :param guest: The guest to check in.
        :param room_number: The number of the room to check in to.
        :param check_in_date: The check-in date in YYYY-MM-DD format.
        :param check_out_date: The check-out date in YYYY-MM-DD format.
        :return: True if the guest was successfully checked in, False otherwise.
        """
        room = self._get_room(room_number)
        if not room.is_available(check_in_date, check_out_date):
            return False
        room.book()
        guest.add_stay(room)
        self.guests.append(guest)
        return True

    def check_out(self, guest: Guest) -> Tuple[bool, int]:
        """
        Checks a guest out of their current room and calculates the bill.

        :param guest: The guest to check out.
        :return: A tuple containing a bool indicating whether the guest was
        successfully checked out and the bill amount.
        """
        room = guest.get_last_stay()
        if not room:
            return False, 0
        check_in_date, check_out_date = room.get_dates(guest)
        bill = room.get_price(check_in_date, check_out_date)
        room.check_out(guest)
        return True, bill

    def get_available_rooms(self, check_in_date: str, check_out_date: str) -> \
    List[int]:
        """
        Returns a list of available room numbers for a given date range.

        :param check_in_date: The check-in date in YYYY-MM-DD format.
        :param check_out_date: The check-out date in YYYY-MM-DD format.
        :return: A list of available room numbers.
        """
        available_rooms = []
        for room in self.rooms:
            if room.is_available(check_in_date, check_out_date):
                available_rooms.append(room.number)
        return available_rooms

    def _get_room(self, room_number: int) -> Room:
        """
        Returns the room instance for a given room number.

        :param room_number: The room number to look up.
        :return: The Room instance for the given room number.
        """
        for room in self.rooms:
            if room.number == room_number:
                return room
        raise ValueError(f"Room {room_number} not found in hotel.")