"""
Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together
the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def print_list(self, l1):
        result = ''
        current = l1
        while current:
            result += str(current.val)
            current = current.next
        return result
    def copy_list(self, l1):
        # !!!!!!!!!!!!!!!!!!!!1 READ THis:
        # http://www.cs.uwm.edu/faculty/boyland/classes-archive/fa15.cs351/www/linked-list-variations.html
        result = ListNode(0)
        current = result
        print('l1: ', self.print_list(l1))
        print('result: ', self.print_list(result))
        print('current: ', self.print_list(current))
        while l1:
            print('before')
            print('l1: ', self.print_list(l1))
            print('result: ', self.print_list(result))
            print('current: ', self.print_list(current))
            current.next = l1
            l1 = l1.next
            current = current.next
            print('after')
            print('l1: ', self.print_list(l1))
            print('result: ', self.print_list(result))
            print('current: ', self.print_list(current))
        # NEED TO INVESTIGATE THE BEHAVIOUR OF CURRENT AND RESULT inside the loop
        # print(result.val)
        # print(result.next.val)
        # print(result.next.next.val)
        # print(result.next.next.next.val)
        # print(result.next.next.next.next.val)
        return result.next

    # def copy_list2(self, l1):
    #     dummy = result = ListNode(0)
    #     while l1:
    #         result.next = l1
    #         l1 = l1.next
    #     result.next = l1
    #     print(dummy.val)
    #     print(dummy.next.val)
    #     print(result.next.next.val)


    # def mergeTwoLists(self, l1, l2):
    #     result = current = ListNode(0)
    #     while l1:
    #         current.next = l1
    #         l1 = l1.next
    #         current.next = l1
    #     print(result.val)
    #     print(result.next.val)
    #     print(result.next.next.val)
        # print(current.val)
        # print(current.next.val)
        # print(current.next.next.val)
    # def mergeTwoLists(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
    #     node = result = ListNode(0)
    #     print(result.val)
    #     while l1:
    #         result.next = l1
    #         l1 = l1.next
    #         result = result.next
    #     print(node.val)
    #     print(node.next.val)
    #     print(node.next.next.val)
    #     print(node.next.next.next.val)
    #     return node
    # def mergeTwoLists1(self, l1, l2):
    #     dummy = cur = ListNode(0)
    #     while l1 and l2:
    #         if l1.val < l2.val:
    #             cur.next = l1
    #             l1 = l1.next
    #         else:
    #             cur.next = l2
    #             l2 = l2.next
    #         cur = cur.next
    #     cur.next = l1 or l2
    #     print(dummy.val)
    #     print(dummy.next.val)
    #     print(dummy.next.next.val)
    #     print(dummy.next.next.next.val)
    #     return dummy.next






L1 = ListNode(1)
nodeL12 = ListNode(2)
nodeL13 = ListNode(3)
nodeL14 = ListNode(4)

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



print(L1.val, L1.next.val)
print(nodeL12.val, nodeL12.next.val)
print(nodeL13.val, nodeL13.next.val)
print(nodeL14.val, nodeL14.next)
# print('Here is list2: ')
#
# print(L2.val, L2.next.val)
# print(nodeL22.val, nodeL22.next.val)
# print(nodeL23.val, nodeL23.next.val)
# print(nodeL24.val, nodeL24.next)


solution = Solution()
print('Implementing')
# print(solution.print_list(L1))
print(solution.copy_list(L1))
# print(solution.copy_list2(L1))


