"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?


"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self, val=None):
        self.head_node = ListNode(val)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = ListNode(new_value)
        new_node.next = self.head_node
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.val != None:
                string_list += " " + str(current_node.val) + "-->"
                # string_list += str(current_node.val) + "\n" + "|->" + "\n"
            current_node = current_node.next
        return string_list

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        check = []
        current = head.get_head_node()
        while current:
            check.append(current.val)
            current = current.next
        node_to_del = len(check)-n
        print('index to delete', node_to_del)
        print('value_to_delete', check[node_to_del])

        current = head.get_head_node()
        while current:
            if current.val == check[node_to_del]:
                next_node = current.next
                current.val = next_node.val
                current.next = next_node.next
                current = next_node
                return
            current = current.next



# head = LinkedList('5')
# head.insert_beginning('4')
# head.insert_beginning('3')
# head.insert_beginning('2')
# head.insert_beginning('1')
head = LinkedList('6')
head.insert_beginning('5')
head.insert_beginning('4')
head.insert_beginning('3')
head.insert_beginning('2')
head.insert_beginning('1')
print(head.stringify_list())
solution = Solution()
print(solution.removeNthFromEnd(head, 3))
print(head.stringify_list())
