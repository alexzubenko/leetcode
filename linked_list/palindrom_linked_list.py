"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # this one more like cheat
    def isPalindrome(self, head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values == values[::-1]
    # well this recursion is works but not for huge inputs
    # def isPalindrome(self, head, end=0, med = 1):
    #     """
    #     :type head: ListNode
    #     :rtype: bool
    #     """
    #     print("---------------------")
    #     if not head:
    #         return True
    #     if med == 0:
    #         return True
    #     dummy = ListNode(0)
    #     dummy.next = head
    #     counter = dummy
    #
    #     check = head.val
    #     print("check", check)
    #
    #     if end==0:
    #         while counter.next:
    #             end +=1
    #             counter = counter.next
    #     count = end
    #     print('the last is ', end)
    #     med = end / 2
    #     while end > 1:
    #
    #         if head.next:
    #           head = head.next
    #         end -=1
    #         print("counter", end)
    #         print("value", head.val)
    #     # print(head.val)
    #     if check != head.val:
    #
    #         print("89495849859458")
    #         print(check)
    #         print(head.val)
    #         return False
    #     else:
    #         return self.isPalindrome(dummy.next.next, count-2, med -1)




head = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(5)
node6 = ListNode(5)
node7 = ListNode(3)
node8 = ListNode(2)
node9 = ListNode(1)
node10 = ListNode(1)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10

# while head:
#     print(str(head.val) + "==>"),
#     head = head.next

solution = Solution()
print(solution.isPalindrome(head))
# print(solution.isPalindrome(head, 0))