"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

class Solution(object):
    """
    To each a specific stair x, we can either climb
     1 stair from x-1, or 2 stairs from x-2. Therefore,
      suppose dp[i] records the number of ways to reach
      stair i, dp[i] = dp[i-1]+dp[i-2]. And it's a Fibonacci Array.
    The base case is to reach the first stair, we only have one way
    to do it so dp[1] = 1.
    Besides, since only dp elements we used is most recent two elements,
     we can use two pointer to save using of dp array. So space complexity is O(1)/
    """
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        current = 1
        prev = 1
        for i in range(n - 1):
            next = current + prev
            current = prev
            prev = next
        return prev
        # a = 1
        # b = 1
        # for i in range(n-1):
        #     c = a + b
        #     a = b
        #     b = c
        # return b


solution = Solution()
print(solution.climbStairs(4))