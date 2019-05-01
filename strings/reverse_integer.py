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

        negative = x < 0 # here is the indicator that it is negative number as a input
        x = abs(x) # for the calculation purpouses transform it to absolute value (module)
        # in other words positive number

        reversed = 0 # set reversed to 0

        while x!=0: # while x is not 0 calculating reversed
            print('Input is: ', x)
            # * 10 here is to move the number to the left
            # like:
            #   3
            #  30
            # 300
            # the main thing is still the leftover from the module operation
            # but rather than adding the leftover to the array and after that
            # transform the array two times
            # first time to array of strings and next time to the int
            # we can simply multiply the intermediate result by 10

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
    #     negative = x < 0 # chek if the number is negative
    #     # to return with - if needed at the end
    #     if x == 0:
    #       return 0
    #
    #     result = []
    #     # Perform calculations on absolute value
    #     # if it -123 - abs value is 123
    #     x = abs(x)
    #
    #     # each time we are adding the leftovers after module operation with 10 to the
    #     # result array and after that dividing the input integer by 10
    #     # doing it while x is not 0
    #     while x != 0:
    #         print('input x: ', x)
    #         number = x%10
    #         print('leftover from diviation : ', number)
    #         result.append(number)
    #         x = x//10
    #         print(result)
    #     # here we should cast the array of integers to array of strings
    #     preresult = [str(i) for i in result]
    #     print(preresult)
    #     # here we are casting the array of strings to the integer
    #     postresult = int(''.join(preresult))
    #     # here we are checking overflow
    #     if postresult > 2 ** 31 - 1:  # checking overflow
    #       return 0
    #     # if we got positive integer as input return the positive
    #     # postresult, otherwise returning the negative postresult
    #     return postresult if not negative else -postresult


solution = Solution()
print(solution.reverse(-123))