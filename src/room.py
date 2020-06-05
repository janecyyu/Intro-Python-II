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
        if len(self.items) is not 0:
            print("\n⬇️ ⬇️ ⬇️ Look!!! ⬇️ ⬇️ ⬇️")
            self.on_take(player)

    def add_item(self, new_item):
        self.items.append(new_item)

    def remove_item(self, remove):
        self.items.remove(remove)

    def on_take(self, player):
        for item in self.items:
            print(item)
            take = input("take or no?")

            if take == 'take' or take == 'get':
                player.add_to_bag(item)
                self.remove_item(item)
                print(f'Ok, you have picked up this "{item.item_name}"!')
            elif take == "no":
                pass
            else:
                print("❓I don't know this.. ❓")

    def on_drop(self, player):
        player.remove_from_bag()
