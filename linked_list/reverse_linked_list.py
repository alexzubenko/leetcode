"""

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively
or recursively. Could you implement both?

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # Iterative solution
    # def reverseList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     prev = None
    #     next = head
    #     while next:
    #         current = next
    #         next = next.next
    #         current.next = prev
    #         prev = current
    #     return prev
    def reverseList(self, head, pre=None):
        if not head: return pre
        print('head: ', head.val)
        cur = head.next
        print('cur', cur.val)
        head.next = pre
        return self.reverseList(cur, head)



head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


solution = Solution()
print(head.val, head.next.val)
print(node2.val, node2.next.val)
print(node3.val, node3.next.val)
print(node4.val, node4.next.val)
print(node5.val, node5.next)

solution = Solution()
print('Implementing')
print(solution.reverseList(head))

# print(head.val, head.next.val)
print(node2.val, node2.next.val)
print(node3.val, node3.next.val)
print(node4.val, node4.next.val)
print(node5.val, node5.next.val)