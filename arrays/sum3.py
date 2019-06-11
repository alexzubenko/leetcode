"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution(object):
    # so far ir works but contains the dublicates in the result
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        validate = {}

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for n in range(i+2,len(nums)):
                    print('---------')
                    print(nums[i])
                    print(nums[j])
                    print(nums[n])
                    if nums[i] + nums[j] + nums[n] == 0:
                        res.append([nums[i], nums[j], nums[n]])
        return res


solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
