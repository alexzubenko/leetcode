'''

1. implement Node class
2. implement LinkedList class
3. implement HashMap class and use LinkedList class to deal with collisions
   use https://www.codecademy.com/paths/computer-science/tracks/complex-data-structures/modules/cspath-hash-maps/projects/blossom
   as a cheat sheet for help
'''


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def get_value(self):
        return self.val

    def set_next_node(self, next_node):
        self.next = next_node

    def get_next_node(self):
        return self.next

class LinkedList:
    def __init__(self, value=None):
        self.head_node = value