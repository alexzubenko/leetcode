"""

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # here we need to return the max sum hence we ill add two variables here
        # max_so_far = 0
        # max_for_the_moment = 0
        #
        # for i in range(len(nums)):
        #     max_for_the_moment = max_for_the_moment + nums[i]
        #     if max_so_far < max_for_the_moment:
        #         max_so_far = max_for_the_moment
        #
        #     if max_for_the_moment < 0:
        #         max_for_the_moment = 0
        # return max_so_far
        # improvements is to check the max_so_far only fo cases whare
        # max_for_the_moment > 0
        # max_so_far = 0
        # max_for_the_moment = 0
        #
        # for i in range(len(nums)):
        #     max_for_the_moment = max_for_the_moment + nums[i]
        #     if max_for_the_moment < 0:
        #         max_for_the_moment = 0
        #
        #     elif max_so_far < max_for_the_moment:
        #           max_so_far = max_for_the_moment
        # if we need to maintain the indexes
        # !!!!!!!!!!!!!!!check it again!!!!!!!
        # max_so_far = 0
        # max_for_the_moment = 0
        # start = 0
        # end = 0
        # the iterator variable here is more like pointer to
        # rememeber the positions where subarray starts ans ends
        # iterator = 0
        #
        # for i in range(len(nums)):
        #     max_for_the_moment = max_for_the_moment + nums[i]
        #     if max_so_far < max_for_the_moment:
        #         max_so_far = max_for_the_moment
        #         start = iterator
        #         end = i
        #
        #     if max_for_the_moment < 0:
        #         max_for_the_moment = 0
        #         iterator = i+1
        # print(nums[start:end+1])
        #
        # return max_so_far
        summ = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            # summ = max(nums[i], summ+nums[i])
            if summ + nums[i] > nums[i]:
                summ +=nums[i]
            else:
                summ = nums[i]
            # res = max(res, summ)
            if res < summ:
                res = summ
        return res

solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
# print(solution.maxSubArray([-1]))