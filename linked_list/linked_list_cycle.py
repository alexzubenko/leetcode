"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.




Follow up:

Can you solve it using O(1) (i.e. constant) memory?

"""


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

    def getTail(self):
        current = self.head_node
        while current.next_node:
            current = current.next_node
        return current

    def setTaillinktohead(self):
        tail_node = self.getTail()
        tail_node.setNextNode(self.head_node)



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

    # def removeNthFromEnd(self,n):
    #     count = 0
    #     current = self.head_node
    #     while current:
    #         current = current.next_node
    #         count +=1
    #     index = count - n
    #     # self.deleteAtIndex(index)
    #     current = self.head_node
    #     while index>1:
    #         current = current.next_node
    #         index -=1
    #     current.next_node = current.next_node.next_node
    def removeNthFromEnd(self, n):
        k = n
        dummy_head = self.head_node
        fast = slow = dummy_head
        while k>0:
            fast = fast.next_node
            k -=1

        while fast and fast.next_node:
            slow = slow.next_node
            fast = fast.next_node

        if slow.next_node:
            slow.next_node = slow.next_node.next_node
        return dummy_head




    # def hasCycle(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: bool
    #     """
    #     seen = {}
    #     while head:
    #         if head in seen:
    #             print('gotcha')
    #             return True
    #         else:
    #             seen[head] = 1
    #             head = head.next_node
    #             # for key,value in seen.items():
    #             #     print(key.getValue())
    #             #     print(value)
    #     return False

    def hasCycle(self, head):
        if not head or not head.next_node:
            return False
        slow = head
        fast = head.next_node

        while slow != fast:
            if not fast or not fast.next_node:
                return False
            slow = slow.next_node
            fast = fast.next_node.next_node
        return True

    def reverse_list(self, head):
        print(head.getValue())
        prev = None
        next = head
        while next:
            current = next
            next = next.next_node
            current.next_node = prev
            prev = current
        return prev





# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList('first element')
obj.addAtHead("second element")
obj.addAtHead("third element")
obj.addAtHead("fourth element")
obj.addAtTail('Last element')
obj.addAtTail('one more Last element')
print(obj.print_list())
# obj.removeNthFromEnd(3)
obj.reverse_list(obj.head_node)
print(obj.print_list())
# print(obj.getTail().getValue())
# obj.setTaillinktohead()
# print(obj.hasCycle(obj.head_node))
# print(obj.print_list())