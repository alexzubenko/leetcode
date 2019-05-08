"""
Given an integer, write a function
to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        power = 3
        if n == 1:
            return True
        while n > power:
            print(n)
            n = n / float(power)
            print(n)
        if n == power:
            return True
        return False
        # power = 3
        # if n == 1:
        #     return True
        # while n >= power:
        #     print(n)
        #     n = n/float(power)
        #     print(n)
        # if n == 1:
        #     return True
        # return False


solution = Solution()
# print(solution.isPowerOfThree(19684))
print(solution.isPowerOfThree(19684))