"""
Given a non-empty array of digits representing
a non-negative integer, plus one to the integer.

The digits are stored such that the most significant
digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading
zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # here we are doing two transformation
        # inside we are casting each element to string
        # with comprehension [str(i) for i in digits]
        # then casting everything to the int
        numbers = int(''.join([str(i) for i in digits]))
        # Adding one to the int
        numbers +=1
        # doing opposite transformation
        # return list([int(i) for i in str(numbers)])
        return [int(i) for i in str(numbers)]


solution = Solution()
print(solution.plusOne([4,3,2,1]))