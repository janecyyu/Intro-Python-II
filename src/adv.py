from room import Room
from player import Player
import textwrap
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Tom", room['outside'])
current_location = player.current_room
game_on = True
# Write a loop that:
while game_on:
    # * Prints the current room name
    print(f"{player.name}, you are at {current_location.name}")
    # # * Prints the current description (the textwrap module might be useful here).
    # # Wrap this text.
    if current_location is not None:
        wrapper = textwrap.TextWrapper(width=100)
        word_list = wrapper.wrap(text=current_location.description)
        print(word_list)
    # * Waits for user input and decides what to do.
    direction = input("select a direction: ")
    direction = direction.lower()
    direction = direction[0]
    # if direction == 'north'
    if direction == 'n':
        # if no more room:
        if current_location.n_to is None:
            print("!!!!no more room this way!!!!")
            pass
        # have room can go
        else:
            current_location = current_location.n_to
    if direction == 's':
        # if no more room:
        if current_location.s_to is None:
            print("!!!!no more room this way!!!!")
            pass
        # have room can go
        else:
            current_location = current_location.s_to
    if direction == 'e':
        # if no more room:
        if current_location.e_to is None:
            print("!!!!no more room this way!!!!")
            pass
        # have room can go
        else:
            current_location = current_location.e_to
    if direction == 'w':
        # if no more room:
        if current_location.w_to is None:
            print("!!!!no more room this way!!!!")
            pass
        # have room can go
        else:
            current_location = current_location.w_to

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
