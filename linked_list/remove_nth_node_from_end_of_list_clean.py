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
    # It works fine for many cases but for leetcode somehow it exeeded the time limit
    def removeNthFromEnd(self, l1, n):
        """
        Time:  O(m)  [m = list length]
        Space: O(1)
        """
        # this will be used for travesre the list first time
        # to get the elements count number
        count = l1
        # those two pointer will be used to check the current value
        # and after all have the one pointer to the head
        # because each time we will traverse the list
        # the "count" pointer will be different
        # and at the end we cannot use it for return
        # hence we have the dummy head
        dummy_head = ListNode(0)
        dummy_head.next = current = l1
        counter = 0
        while count:
            counter += 1
            count = count.next
        if counter == 1 and n==1:
            current.val = None
            current.next = dummy_head
            return dummy_head
        print('we counted ', counter)
        wtd = counter - n
        print('wtd', wtd)
        while wtd > 0:
            # prev here to treak the previous node
            # in case if we should delete the last node
            prev = current
            # print(l1.val)
            current = current.next
            wtd -= 1
        print('wtd: ', wtd)
        print('current node value: ', current.val)

        # Now we got the node which should be deleted
        # from the list and what we do is to pint the current
        # node to the next node
        # and set the value for the current done to the
        # next's node value
        # but before that we should check if it is not the last node in the list
        # because if is we should vanish the current node and not
        # pointing it to nothing
        if current.next:
            current.val = current.next.val
            current.next = current.next.next
        else:
            current.nextv = prev
            prev.next = None
        return dummy_head.next

head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

# head.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# node5.next = node6

solution = Solution()
input = head
print('Input: ')
while head:
    print(head.val)
    head = head.next
print("Implementation")
result = solution.removeNthFromEnd(input, 1)
print(result.val)
# while result:
#     print(result.val)
#     result = result.next


