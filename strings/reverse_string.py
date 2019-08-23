"""
Write a function that reverses a string.
The input string is given as an array of characters char[].

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.


Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


"""

class Solution(object):
    def reverseString(self, s):
        index = len(s)
        # print('before', s)
        while index>1:
            # print(index)
            # print(s[0])
            s.insert(index,s[0])
            s.pop(0)
            # print('after', s)
            index -=1
        return s
    # First solution is very easy but it does not work on leetcode
    # def reverseString(self, s):
    #     """
    #     :type s: List[str]
    #     :rtype: None Do not return anything, modify s in-place instead.
    #     """
    #     return s[::-1]
    # another variant
    # def reverseString(self, s):
    #     s.reverse()
    #     return s
    #
    # this one i like but in leetcode it does not work somehow
    # def reverseString(self, s):
    #     m = len(s)
    #     s = list(s)
    #     for i in range(m//2):
    #         s[i], s[~i] = s[~i], s[i]
    #     return s
    # This is the another way but doesnt work on leetcode as well
    # def reverseString(self, s):
    #     reverse = []
    #     for i in range(len(s)-1,-1,-1):
    #         reverse.append(s[i])
    #     return reverse





solution = Solution()
# print(solution.reverseString(["H","a","n","n","a","h"]))
print(solution.reverseString(["H","e","l","l","o"]))