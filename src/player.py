# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, bag):
        self.name = name
        self.current_room = current_room
        self.bag = bag

    def print_bag(self):
        for i in self.bag:
            print("I got: " + i.item_name)

    def add_to_bag(self, item):
        self.bag.append(item)

    def remove_from_bag(self, item):
        self.bag.remove(item)
