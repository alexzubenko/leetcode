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

    def removeElements(self, val, head):
        head_holder = ListNode(-1)
        head_holder.next = head

        current = head_holder
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return head_holder.next


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
sol.removeElements(6, node1)
print(sol.print_list(node1))

