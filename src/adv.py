from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# print(room['outside'].n_to)
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input("What is your name? "), room['outside'])

print(f"Hello, {player.name}.")

# player_one = Player('Player', room['outside']) my code

while True:
    print(f'You are currently {player.current_room}')
    cmd = input("->").lower()
    if cmd in ["n", "s", "e", "w"]:
        # move to that room
        # print("You went " + cmd)
        if cmd == "n":
            if player.current_room.n_to != None:
                player.current_room = player.current_room.n_to
            else:
                print("You cannot move in that direction!")
        if cmd == "s":
            if player.current_room.s_to != None:
                player.current_room = player.current_room.s_to
            else:
                print("You cannot move in that direction!")
        if cmd == "e":
            if player.current_room.e_to != None:
                player.current_room = player.current_room.e_to
            else:
                print("You cannot move in that direction!")
        if cmd == "w":
            if player.current_room.w_to != None:
                player.current_room = player.current_room.w_to
            else:
                print("You cannot move in that direction!")
    elif cmd == "q":
        print(f"Goodbye {player.name}")
        exit()
    else:
        print("I did not understand that command.")


# my original code
# # Write a loop that:
# #
# done = False
# while not done:
#     current_room = player_one.current_room
#     print(player_one)

#     user_input = input("enter a command: ")
#     # exiting the program
#     if user_input == 'q':
#         done = True

#     if user_input == 'w':
#         if current_room.w_to:
#             player_one.current_room = current_room.w_to
#     elif user_input == 'e':
#         if current_room.e_to:
#             player_one.current_room = current_room.e_to
#     elif user_input == 's':
#         if current_room.s_to:
#             player_one.current_room = current_room.s_to
#     elif user_input == 'n':
#         if current_room.n_to:
#             player_one.current_room = current_room.n_to
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Add a REPL parser to adv.py that accepts directional commands to move the player

# After each move, the REPL should print the name and description of the player's current room
# Valid commands are n, s, e and w which move the player North, South, East or West
# The parser should print an error if the player tries to move where there is no room.
