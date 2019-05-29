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

# class LinkedList:
#     def __init__(self, val=None):
#         self.head_node = ListNode(val)
#
#     def get_head_node(self):
#         return self.head_node
#
#     def insert_beginning(self, new_value):
#         new_node = ListNode(new_value)
#         new_node.next = self.head_node
#         self.head_node = new_node
#
#     def stringify_list(self):
#         string_list = ""
#         current_node = self.get_head_node()
#         while current_node:
#             if current_node.val != None:
#                 string_list += " " + str(current_node.val) + "-->"
#                 # string_list += str(current_node.val) + "\n" + "|->" + "\n"
#             current_node = current_node.next
#         return string_list

# class Solution(object):
#     # FAILING with input like [1,2]
#     def removeNthFromEnd(self, head, n):
#         """
#         :type head: ListNode
#         :type n: int
#         :rtype: ListNode
#         """
#         check = []
#         current = head
#         while current:
#             check.append(current.val)
#             current = current.next
#         node_to_del = len(check)-n
#         print(check)
#         print('index to delete', node_to_del)
#         print('value_to_delete', check[node_to_del])
#         if len(check) == 1:
#             return head
#
#         current = head
#         while current:
#             print(current.val)
#             if current.val == check[node_to_del]:
#                 # print('got it')
#                 if not current.next:
#                     return head
#                 next_node = current.next
#                 current.val = next_node.val
#                 current.next = next_node.next
#                 current = next_node
#             current = current.next
#         return head

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        Time:  O(m)  [m = list length]
        Space: O(1)
        """
        ahead = head
        print('ahead: ',ahead.val)
        for i in range(n):
            print('iterator: ', i)
            ahead = ahead.next

        if not ahead:
            print('no ahead')
            return head.next

        behind = head
        print('behind: ', behind.val)
        while ahead.next:
            print('ahead.next: ', ahead.next)
            ahead = ahead.next
            print('ahead: ', ahead.next)
            behind = behind.next
        behind.next = behind.next.next
        return head

    # def removeNthFromEnd(self, head, n):
    #     """
    #     Time:  O(m)  [m = list length]
    #     Space: O(1)
    #     """
    #     ahead = head
    #     print('ahead: ',ahead.val)
    #     for i in range(n):
    #         print('iterator: ', i)
    #         ahead = ahead.next
    #
    #     if not ahead:
    #         print('no ahead')
    #         return head.next
    #
    #     behind = head
    #     print('behind: ', behind.val)
    #     while ahead.next:
    #         print('ahead.next: ', ahead.next)
    #         ahead = ahead.next
    #         print('ahead: ', ahead.next)
    #         behind = behind.next
    #     behind.next = behind.next.next
    #     return head



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
print(solution.removeNthFromEnd(head, 4))
#
# print(head.val, head.next.val)
# print(node2.val, node2.next.val)
# print(node3.val, node3.next.val)
# print(node4.val, node4.next.val)
# print(node5.val, node5.next)

