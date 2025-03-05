from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")


    def add_room(self, room: Room):
        self.rooms.append(room)


    def take_room(self, room_number, people):
        room = next((room for room in self.rooms if room.number == room_number), None)

        if room and room.capacity >= people:
            room.is_taken = True
            room.guests = people
            self.guests += people


    def free_room(self, room_number):
        room = next((room for room in self.rooms if room.number == room_number), None)

        if room and room.is_taken:
            room.is_taken = False
            self.guests -= room.guests
            room.guests = 0


    def status(self):
        total_guest = sum(room.guests for room in self.rooms)
        output = [f"Hotel {self.name} has {total_guest} total guests"]

        free_rooms = [room.number for room in self.rooms if not room.is_taken]
        taken_rooms = [room.number for room in self.rooms if room.is_taken]

        output.append(f"Free rooms: {', '.join(map(str, free_rooms))}")
        output.append(f"Taken rooms: {', '.join(map(str, taken_rooms))}")

        return '\n'.join(output)



