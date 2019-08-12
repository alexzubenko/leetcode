class Solution(object):
    # this one works
    def binary_search(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if target == nums[mid]:
                return mid
            else:
                if target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
        return -1

sol = Solution()
# print(sol.binary_search([-1, 0, 3, 5, 9, 12], 9))
print(sol.binary_search([-1, 0, 3, 5, 9, 12, 31, 333, 433, 555, 777], 333))