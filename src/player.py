# Write a class to hold player information, e.g. what room they are in
# currently.
# https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/

# Put the Player class in player.py.

# Players should have a name and current_room attributes


from room import Room


class Player:
    def __init__(self, name, current_room=None):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        output = f'{self.name}, your current location is in the {self.current_room}.'

        return output
