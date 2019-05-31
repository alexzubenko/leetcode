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


class Solution:
    def removeNthFromEnd(self, node, n):
        """
        Time:  O(m)  [m = list length]
        Space: O(1)
        """
        if not node or n == 0:
            return node
        dummy_head  = ListNode(0)
        dummy_head.next = node
        slow = fast = dummy_head
        k = n
        while k > 0:
            fast = fast.next
            k -= 1
        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        if slow.next:
            slow.next = slow.next.next
        return dummy_head.next





head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

solution = Solution()
input = head
print('Input: ')
while head:
    print(head.val)
    head = head.next
print("Implementation")
result = solution.removeNthFromEnd(input, 2)
# print(result.val)
while result:
    print(result.val)
    result = result.next


