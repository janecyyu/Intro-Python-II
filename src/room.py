# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


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

    def add_item(self, new_item):
        self.items.append(new_item)
