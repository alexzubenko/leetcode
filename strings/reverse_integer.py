"""

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could
only store integers within the 32-bit signed integer
range: [−231,  231 − 1]. For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows.
"""


class Solution(object):
    # here is the solution from discussion
    #!!!!!! PLEASE COMPARE my and their to remember!!!
    def reverse(self, x):
        print('Input is: ', x)

        negative = x < 0 # here is the indicator that it is negative number as a input
        x = abs(x) # for the calculation purpouses transform it to absolute value (module)
        # in other words positive number

        reversed = 0 # set reversed to 0

        while x!=0: # while x is not 0 calculating reversed
            reversed = reversed * 10 + x % 10
            print('reversed is: ', reversed)
            x//=10
            print('x is: ', x)
            print('----------')

        if reversed > 2**31 -1: # checking overflow
            return 0
        return reversed if not negative else -reversed # checking if we got negative
        # number as a input and return negative result
    # # this was the my solution which does not correctly seems
    # def reverse(self, x):
    #     """
    #     :type x: int
    #     :rtype: int
    #     """
    #     if x > 231 or x < -231 or x == 0:
    #         return 0
    #     if x < 0 and x > -231:
    #         x = x * -1
    #         result = ['-']
    #     else:
    #         result = []
    #
    #     step = 0
    #     while x != 0:
    #         number = x%10
    #         result.append(number)
    #         x = x//10
    #         step += 1
    #         print(result)
    #     preresult = [str(i) for i in result]
    #     return int(''.join(preresult))


solution = Solution()
print(solution.reverse(230))