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

    def isPalindrom(self,head):
        if not head:
            return None
        check = {}
        cur = head
        while cur:
            if cur.val not in check:
                check[cur.val] = 1
            else:
                check[cur.val] +=1
            cur = cur.next
        for key in check.keys():
            if check[key] == 1:
                return False
        return True

    def isPalindrom2(self, head):
        result = []
        cur = head
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result == result[::-1]

    # this is the standard linked list reverse
    # technic with two pointers
    def reverse(self, head):
        if not head:
            return None
        prev = None
        tocheck = head
        while tocheck:
            cur = tocheck
            tocheck = tocheck.next
            cur.next = prev
            prev = cur
        return prev
    def isPalindrom3(self, head):
        # 1. find where the second part of the list starts (secondHead)
        # 2. reverse the second part
        # 3. traverse from head and secondHead respectively and compare the values

        # here we have two pointers fast will go ahead two times faster each
        # time, therefor when it got to the finish the slow pointer will
        # be exactly in the middle of the linked list and
        # give us a point where we need to start the reverse operation
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if not fast:
            secondHead = slow
        else:
            secondHead = slow.next
        secondHead = self.reverse(secondHead)

        while head and secondHead:
            if head.val != secondHead.val:
                return False
            head = head.next
            secondHead = secondHead.next
        return True


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(2)
node6 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

sol = Solution()
print(sol.print_list(node1))
# sol.reverse(node1)
# print(sol.print_list(node5))
# print(sol.isPalindrom(node1))
# print(sol.isPalindrom2(node1))
print(sol.isPalindrom3(node1))