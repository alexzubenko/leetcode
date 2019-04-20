"""
Given a sorted array nums, remove the duplicates in-place
such that each element appear only once and return the new length.

Given nums = [1,1,2],

Your function should return length = 2,
with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.


Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5,
with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.

"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        index = 1
        while index < len(nums):
            if nums[index] == nums[index-1]:
                nums.pop(index)
            else:
                index += 1
        return len(nums)




solution = Solution()

print(solution.removeDuplicates([1,2,3,3,3,3,3,3,3]))