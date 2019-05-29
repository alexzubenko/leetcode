"""
Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together
the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

Some explanation from myself:
above statement means that we should not simply copy all elements
to the result list, but sort them and pick only element which is lesser

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def copy_list(self,l1):
        # First and foremoust you should remember about linked list
        # Is that we are not returning the list itself, but pointer
        # here we need to create two pointers
        # One is the dummy head, which will always
        # be pointing to the head of the new "linked list"
        # The another is the current pointer which will help us to build the
        # new linked list
        dummy_head = current = ListNode(0)
        while l1:
            current.next = l1
            l1 = l1.next
            current = current.next
        # here we should return the pointer which point to the
        # head of our new linked list, the structure is the following
        # dummy_head --> current -->
        # therefore we should return the dummy_head.next pointer
        return dummy_head.next

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_head = current = ListNode(0)
        # here we are checking which value is less and using it
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        # once we traversed through 2 arrays it can be the point when
        # many items are still left unchecked in one of the array,
        # it happens when arrays are not equal by size.
        # then we are checking in which array are elements left and point
        # our current.next to it
        # it can be done just by checking if the array is still true
        # and if yes, then it still contains the elements
        current.next = l1 or l2
        # or instead we can use less fancier statement:
        # if l1:
        #     current.next = l1
        # if l2:
        #     current.next = l1
        return dummy_head.next



L1 = ListNode(1)
nodeL12 = ListNode(20)
nodeL13 = ListNode(5)
nodeL14 = ListNode(15)

L1.next = nodeL12
nodeL12.next = nodeL13
nodeL13.next = nodeL14

L2 = ListNode(5)
nodeL22 = ListNode(6)
nodeL23 = ListNode(7)
nodeL24 = ListNode(8)

L2.next = nodeL22
nodeL22.next = nodeL23
nodeL23.next = nodeL24


solution = Solution()
print('Implementing')
# result = solution.copy_list(L1)
result = solution.mergeTwoLists(L1,L2)
while result:
    print(result.val)
    result = result.next




