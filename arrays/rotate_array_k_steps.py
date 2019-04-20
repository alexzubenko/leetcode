'''

Given an array, rotate the array to the right by k steps, where k is non-negative.

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

'''

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
          nums.insert(0,nums[-1])
          nums.pop(-1)
        return nums
solution = Solution()

print(solution.rotate([1,2,3,4,5,6,7], 4))
print(solution.rotate([-1,-100,3,99], 2))


