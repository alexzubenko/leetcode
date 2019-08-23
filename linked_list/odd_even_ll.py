class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):

    def print_list(self, head):
        current = head
        out = 'here is our list: \n'
        while current:
            out += str(current.val) + '-->'
            current = current.next

        return out

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        odd = head
        even = odd.next
        evenHead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head




node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
sol = Solution()
print(sol.print_list(node1))
sol.oddEvenList(node1)
print(sol.print_list(node1))
