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
        if len(self.items) is not 0:
            for item in self.items:
                print(item)
                take = input("take it?")

                if take == 'take' or take == 'get':
                    player.add_to_bag(item)
                    self.remove_item(item)
                    return print(f'Ok, you have picked up this "{item.item_name}"!')
                if take == "no":
                    pass
        else:
            print("Sorry, It's empty..")

    def add_item(self, new_item):
        self.items.append(new_item)

    def remove_item(self, remove):
        self.items.remove(remove)
