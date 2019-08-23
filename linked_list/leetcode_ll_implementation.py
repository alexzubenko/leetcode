class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def getValue(self):
        return self.value

    def getNextNode(self):
        return self.next_node

    def setValue(self, value):
        self.value = value

    def setNextNode(self, next_node):
        self.next_node = next_node


class MyLinkedList(object):

    def __init__(self, value=None):
        """
        Initialize your data structure here.
        """
        self.head_node = Node(value)



    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        # print('starting searching for index: ', index)
        current = self.head_node
        # print(current.getValue())
        localIndex = 0
        while current:
            if localIndex == index:
                return current
            else:
                localIndex +=1
                current = current.getNextNode()
        return current

    def print_list(self):
        represent = 'Here is our list: \n'
        current = self.head_node
        index = 0
        while current:
            represent += current.getValue() + ' index:' + str(index) + ' --> '
            index += 1
            current = current.getNextNode()

        return represent

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: string
        :rtype: None
        """
        current = Node(val)
        current.next_node = self.head_node
        self.head_node = current

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        last_node = Node(val)
        current = self.head_node
        while current.next_node:
            current = current.next_node
        current.setNextNode(last_node)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        node_to_insert = Node(val)
        prev = self.head_node
        current = prev.getNextNode()
        start_index = 0
        while current:
            if start_index == index:
                print('got here')
                prev.setNextNode(node_to_insert)
                node_to_insert.setNextNode(current)
                break
            else:
                start_index +=1
                prev = prev.getNextNode()
                current = current.getNextNode()



    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        print('starting deletion on index: ', index)
        prev = self.get(index-1)
        current = self.get(index)
        next = current.getNextNode()
        prev.setNextNode(next)



# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList('first element')
# print(obj.head_node.getValue())
# print(obj.get(0).getValue())
obj.addAtHead("second element")
obj.addAtHead("third element")
obj.addAtHead("fourth element")
# print(obj.print_list())
# print(obj.head_node.getValue())
# print(obj.get(1).getValue())
obj.addAtTail('Last element')
obj.addAtTail('one more Last element')
print(obj.print_list())
# print(obj.get(2).getValue())
# print(obj.print_list())
# obj.addAtIndex(0,'New value inserted')
# print(obj.print_list())
obj.deleteAtIndex(2)
print(obj.print_list())
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)