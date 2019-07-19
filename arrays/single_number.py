"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/

Given a non-empty array of integers,
 every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity.
 Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

"""


"""
BAD one (too slow):

class Solution(object):
    def singleNumber(self, nums):
        for i in nums:
            if nums.count(i) == 1:
                return i
        


"""

# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort()
#         print(nums)
#         uniq = None
#         for i in range(len(nums)):
#             print('-------')
#             print(uniq)
#             print(nums[i])
#             print(nums[i+1:])
#             if nums[i] not in nums[i+1:] and uniq != nums[i]:
#                 print('got it')
#                 return nums[i]
#             else:
#                 uniq = nums[i]
#         return uniq

# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         uniq = []
#         for i in range(len(nums)):
#             if nums[i] not in nums[i+1:] and nums[i] not in uniq:
#                 print('got it')
#                 return nums[i]
#             else:
#                 uniq.append(nums[i])
#         return uniq

class Solution(object):
    # this one works good but uses addional memory
    def singleNumber(self, nums):
        testik = {}
        for i in nums:
            if i in testik:
                testik[i] = 1
            else:
                testik[i] = 0
        for key in testik.keys():
            if testik[key] == 0:
                return key

    # this one works like a charm but nor for huge input
    # def singleNumber(self, nums):
    #     if len(nums) == 1:
    #         return nums[0]
    #     while True:
    #         if nums[0] not in nums[1:]:
    #             return nums[0]
    #         else:
    #             nums = [z for z in nums if z!=nums[0]]

    # def singleNumber(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     uniq = {}
    #     for i in nums:
    #         if i in uniq:
    #             print('yes')
    #             uniq[i] = 0
    #             print(uniq[i])
    #         else:
    #             print('nope')
    #             uniq[i] = 1
    #             print(uniq[i])
    #         print(uniq)
    #
    #     for i in uniq.keys():
    #         if (uniq[i] == 1):
    #             return i



solution = Solution()
# print(solution.singleNumber([2,2,1,1,8]))
# print(solution.singleNumber([4,1,2,1,2]))
# print(solution.singleNumber([2,2,1]))
# print(solution.singleNumber([1,0,1]))
# print(solution.singleNumber([1]))

