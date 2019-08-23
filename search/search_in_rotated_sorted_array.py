class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1 and nums[0] == target:
            return 0
        elif len(nums) == 1 and nums[0] != target:
            return -1

        def findRotatedPoint(left, right):
            if nums[left] < nums[right]:
                return 0
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > nums[mid + 1]:
                    return mid + 1
                else:
                    if nums[mid] < nums[0]:
                        right = mid - 1
                    else:
                        left = mid + 1
            return -1

        def binarysearch(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                else:
                    if target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
            return -1

        rotationPoint = findRotatedPoint(0, len(nums) - 1)
        print(rotationPoint)

        if rotationPoint == 0:
            return binarysearch(0, len(nums) - 1)
        if target < nums[0]:
            return binarysearch(rotationPoint, len(nums) - 1)
        else:
            return binarysearch(0, rotationPoint)


sol = Solution()
# print(sol.search([4,5,6,7,0,1,2],1))
# print(sol.search([4,5,6,7,0,1,2],4))
print(sol.search([1,3],4))