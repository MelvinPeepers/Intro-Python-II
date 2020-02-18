# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        output = f'Welcome {self.name} to the game. Your location is in the {self.current_room} room.'

        return output
