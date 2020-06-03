# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        output = f'{self.name}'
        return output

    def n_to(self, n_to):
        return self.n_to

    def south(self, s_to):
        return self.s_to

    def w(self, w_to):
        return self.w_to

    def e(self, e_to):
        return self.e_to
