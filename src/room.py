# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
from player import Player


class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.items = items

    def __str__(self):
        output = f'{self.name,self.description}'
        return output

    def print_items(self, player):
        print("\n⬇️ ⬇️ ⬇️ You found this ⬇️ ⬇️ ⬇️")
        for item in self.items:
            print(item)
            take = input("take it?")

            if take == 'take' or take == 'get':
                player.add_to_bag(item)
                print(f'Ok, you take this "{item.item_name}"!')

    def add_item(self, new_item):
        self.items.append(new_item)
