"""

Given an array of integers, find if the array
contains any duplicates.

Your function should return true if any value
appears at least twice in the array, and it should
return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

"""


class Solution(object):
    # first solution with O(n2)
    # def containsDuplicate(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] == nums[j]:
    #                 return True
    #         return False

    # second solution with O(n)
    def containsDuplicate(self, nums):
        print(nums)
        check = {}
        for i in nums:
            if i in check:
                check[i] = 0
            else:
                check[i] = 1
        print(check)
        for key in check.keys():
            print(check[key])
            if check[key] == 0:
                return True
        return False
    # one liner solution with using set
    # def containsDuplicate(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     return len(nums) != len(set(nums))


solution = Solution()
print(solution.containsDuplicate([2,14,18,22,22]))