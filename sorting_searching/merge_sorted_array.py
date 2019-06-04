"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # first we should create several pointers
        l1 = m-1 # index of the last number in first array
        l2 = n-1 # index of the last number in second array
        end = m+n-1 # index of the last element in the first array

        while l1 >=0 and l2 >=0:
            # if the last element from second array is bigget than in first,
            # put it in to the end of the first array
            if nums2[l2] > nums1[l1]:
                nums1[end] = nums2[l2]
                # reduce the index to check different element next time
                l2 -=1
            else:
                # else get the element from the first array
                nums1[end] = nums1[l1]
                l1 -= 1
            # reducing the end index to insert to the next available place
            end -=1
        if l1 < 0: # in such way we are checking ig anything left in second array
            # and if it does we put it to the right place of the first array
            nums1[:l2+1] = nums2[:l2+1]



    # this variant works for the case where we need to return new array
    # def merge(self, nums1, m, nums2, n):
    #     result = []
    #     if m <= n:
    #       while nums1:
    #           if nums1[0] <= nums2[0]:
    #               result.append(nums1[0])
    #               nums1.pop(0)
    #           else:
    #               result.append(nums2[0])
    #               nums2.pop(0)
    #       result = result + nums2
    #     else:
    #         while nums2:
    #             if nums1[0] <= nums2[0]:
    #                 result.append(nums1[0])
    #                 nums1.pop(0)
    #             else:
    #                 result.append(nums2[0])
    #                 nums2.pop(0)
    #         result = result + nums1
    #     return result





solution = Solution()
print(solution.merge([1,3,4,5], 4, [2, 4, 6, 8 ,9,10], 6))
print(solution.merge([1,2,3], 3, [2,5,6], 3))
