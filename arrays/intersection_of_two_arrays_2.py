"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear
 as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted?
 How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size?
 Which algorithm is better?
What if elements of nums2 are stored on disk,
 and the memory is limited such that you cannot load
  all elements into the memory at once?

"""

from collections import Counter


class Solution(object):
    # Counter solution
    def intersect(self, nums1, nums2):
        result = []
        c1 = Counter(nums1)
        # print(c1)
        for i in nums2:
            if i in c1 and c1[i] > 0:
                result.append(i)
                c1[i] -= 1
        return result
    # # solution using dictionary
    # def intersect(self, nums1, nums2):
    #     result = []
    #     dictik = {}
    #     for i in nums1:
    #         # in python2 it will fail if there is no key in dic
    #         # need to use dictik.has_key() instead
    #         if i in dictik:
    #             dictik[i]+=1
    #         else:
    #             dictik[i] = 1
    #     # print(dictik)
    #     for i in nums2:
    #         if i in dictik and dictik[i] > 0:
    #             result.append(i)
    #             dictik[i] -=1
    #     return result

    # # this solution will add the each intersection
    # # to the result array and remove it from the second array
    # # to do not count it several times
    # def intersect(self, nums1, nums2):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: List[int]
    #     """
    #     result = []
    #     for i in nums1:
    #         if i in nums2:
    #             result.append(i)
    #             nums2.remove(i)
    #     return result
    #     # for i in range(len(nums1)):
    #     #     if nums1[i] in nums2:
    #     #         result.append(nums1[i])
    #     #         nums2.remove(nums1[i])
    #     # return result


solution = Solution()
print(solution.intersect([1,2,2,1], [2,2]))
print(solution.intersect([4,9,5], [9,4,9,8,4]))
print(solution.intersect([0,0,0,0], [0]))
print(solution.intersect([1,2], [2,1]))