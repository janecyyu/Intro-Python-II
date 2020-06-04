# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, bag):
        self.name = name
        self.current_room = current_room
        self.bag = bag

    def print_bag(self):
        for i in self.bag:
            print(i)

    def add_to_bag(self, item):
        self.bag.append(item)
