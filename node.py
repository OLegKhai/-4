from cat import Cat


class Node:
    def __init__(self, cat):
        self.cat = cat
        self.next = None

    def __repr__(self):
        return str(self.cat)
