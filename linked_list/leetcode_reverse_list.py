# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def print_list(self, head):
        current = head
        out = 'here is our list: \n'
        while current:
            out += str(current.val) + '-->'
            current = current.next

        return out

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fake_head = None
        next_node = head
        while next_node:
            current_node = next_node
            next_node = next_node.next
            current_node.next = fake_head
            fake_head = current_node
        return fake_head
        # prev = None
        # next = head
        # while next:
        #     current = next
        #     next = next.next
        #     current.next = prev
        #     prev = current
        # return prev


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
sol = Solution()
print(sol.print_list(node1))
sol.reverseList(node1)
print(sol.print_list(node5))
