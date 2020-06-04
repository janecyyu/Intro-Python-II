from room import Room
from player import Player
import textwrap
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Chihuahua puppy", "Aww~ She is smiling..🐶")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
    passages run north and east.""", [Item("TV", "It's playing news..📺")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
    into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", [Item("Face Mask", "Wearing it can prevent virus!😷"), Item("Apple", "An apple a day, keep the doctor away!🍎")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""", [Item("Bee", "but it's friendly..🐝"), Item("Honey", "Yum yum!🍯")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""", [Item("Teddy Bear", "So cute!🐻")]),
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


def no_outlet():
    print("🙅‍!!!!no more room this way!!!!🙅")
    pass

#
# Main
#


# Make a new player object that is currently in the 'outside' room.
player = Player("Tom", room['outside'], [])
current_room = player.current_room
game_on = True
# Write a loop that:
while game_on:
    # * Prints the current room name
    print(f"\n{player.name}, you are at {current_room.name}")
    # # * Prints the current description (the textwrap module might be useful here).
    # # Wrap this text.
    if current_room is not None:
        wrapper = textwrap.TextWrapper()
        word_list = wrapper.wrap(text=current_room.description)
        print(word_list)
    # print items
    current_room.print_items(player)
    # * Waits for user input and decides what to do.
    direction = input("\nselect a direction - n, e, w, s: ")
    direction = direction.lower()
    direction = direction[0]
    # if direction == 'north'
    if direction == 'n':
        # if no more room:
        if current_room.n_to is None:
            no_outlet()
        # have room can go
        else:
            current_room = current_room.n_to

    elif direction == 's':
        # if no more room:
        if current_room.s_to is None:
            no_outlet()
        else:
            current_room = current_room.s_to
    elif direction == 'e':
        # if no more room:
        if current_room.e_to is None:
            no_outlet()
        else:
            current_room = current_room.e_to
    elif direction == 'w':
        # if no more room:
        if current_room.w_to is None:
            no_outlet()
        else:
            current_room = current_room.w_to
    elif direction == 'q':
        game_on = False

    else:
        print("❓I don't know what this means. Try again please!❓")

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
