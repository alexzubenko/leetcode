"""

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


class Solution(object):
    # backwards solution
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1, 0, -1):
            if target - nums[i] in nums[:i]:
                return [nums.index(target-nums[i]), i]

    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     for i in range(len(nums)):
    #         if target - nums[i] in nums[i+1:]:
    #             print(i)
    #             print(target - nums[i])
    #             print('hreey')
    #             return [i, nums.index(target - nums[i])]



solution = Solution()
print(solution.twoSum([3,2,3], 6))