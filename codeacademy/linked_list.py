# We'll be using our Node class
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


# Our LinkedList class
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        output = ""
        current_node = self.head_node
        while current_node:
            output = output + str(current_node.get_value()) + '\n'
            current_node = current_node.get_next_node()
        return output

    def remove_node(self, value_to_remove):
        current_node = self.head_node
        if current_node.get_value() == value_to_remove:
            self.head_node = self.head_node.get_next_node()
        else:
            print('got here')
            while current_node:
                print('the current node value is ', current_node.get_value())
                if current_node.get_next_node().get_value() == value_to_remove:
                    print('got even here this time')
                    current_node.set_next_node(current_node.get_next_node().get_next_node())
                    current_node = None
                else:
                    current_node = current_node.get_next_node()


# Add your insert_beginning and stringify_list methods below:


# Test your code by uncommenting the statements below - did your list print to the terminal?
ll = LinkedList(5)
ll.insert_beginning(11)
ll.insert_beginning(66)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())

print('----------------------------'
)

ll.remove_node(5675)
print(ll.stringify_list())