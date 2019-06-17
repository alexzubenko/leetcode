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
    # https://leetcode.com/problems/3sum/discuss/232712/Best-Python-Solution-(Explained)
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # this new array will store the result triplets
        res = []
        print('initial array: ', nums)
        # to easy the work we need to sort the initial array
        nums.sort()
        print('sorted array: ', nums)
        # here we are iteratim through array till last two numbers
        for i in range(len(nums)-2):
            print('the number we are checking is the: ', nums[i])
            # the following statement will check two things
            # the first if the index > 0 and
            # check if the target number the same as prev skip it
            # because if we are checking the first number in the array
            # as a target we can be sure that we have nor checked it yet
            # but starting from the second element in the array
            # as a target we need to make sure we have not tried it already
            # as a target and if so, skip it
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # here is two pointers for start and end,
            # we are going to summ those numbers with current i
            left, right = i+1, len(nums)-1
            # due to fact that array is sorted we
            # can consider that when the following is not true
            # it will be the middle of the array and
            # we will iterate through all numbers till the middle point
            while left < right:
                print("Outer while begins!!!!!!!!!")
                print("left number is: ", nums[left])
                print("right number is: ", nums[right])
                print("the triplet we are checking is ["
                      "{}, {}, {}]".format(nums[i], nums[left], nums[right]))
                # calculating the sum of tree numbers
                summa = nums[i] + nums[left] + nums[right]
                # due to face that array id sorted we would know that if we
                # need the bigger sum we can move the left pointer to the right
                # and if we need less we can move the right pointer to the left
                # and the goal here actually is to find the sum = 0
                if summa < 0:
                    print("the sum is less than zero, increasing left pointer")
                    print("left pointer was {}".format(nums[left]))
                    left +=1
                    print("left pointer now is {}".format(nums[left]))
                elif summa > 0:
                    print("the sum is bigger than zero, decreasing right pointer")
                    print("right pointer was {}".format(nums[right]))
                    right -=1
                    print("right pointer now is {}".format(nums[right]))
                else:
                    # bingo, we found the sum = 0 and adding the triplet to the res
                    print("bingo")
                    print(nums[i])
                    print(nums[left])
                    print(nums[right])
                    res.append([nums[i], nums[left], nums[right]])
                    # the following code is required to avoid checking the
                    # numbers we already checked as a lefr and right, in such
                    # way we can avoid the duplicades in the result array,
                    # as a exemple we can check this input [-2, 0, 0, 2, 2]
                    # without the below block the result is gonna be
                    # the [[-2, 0, 2], [-2, 0, 2]] due to repeated numbers
                    # in the input, with this block the result would
                    # be the [[-2, 0, 2]]
                    while left < right and nums[left] == nums[left + 1]:
                        print("Inner left while begins!!!!!!!!!")
                        print("nums[left] is the same as the next one", nums[left])
                        left +=1
                        print("increased nums[left] is: {}".format(nums[left]))
                    while left < right and nums[right] == nums[right -1]:
                        print("Inner right while begins!!!!!!!!!")
                        print("nums[right] is the same as the next one", nums[right])
                        right -=1
                        print("decreased nums[right] is: ", nums[right])
                    left +=1
                    right -=1
        return res








    #  # so far ir works but not for all cases, hence it should be rewrited
    # def threeSum(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     print('initial list: ', nums)
    #     ress = []
    #
    #     for i in range(len(nums)):
    #         for j in range(i+1,len(nums)):
    #             for n in range(i+2,len(nums)):
    #                 if nums[i] + nums[j] + nums[n] == 0:
    #                     ress.append([nums[i], nums[j], nums[n]])
    #     print(ress)
    #     for i in ress:
    #         i.sort()
    #     print(ress)
    #     ress.sort()
    #     print(ress)
    #     count = 0
    #     while count < len(ress)-1:
    #         if ress[count] == ress[count+1]:
    #             ress.remove(ress[count])
    #         else:
    #             count +=1
    #     return ress


solution = Solution()
print(solution.threeSum([-2,0,0,2,2]))
# print(solution.threeSum([1,2,-2,-1]))
# print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
# print(solution.threeSum([-1, -1, -2, -2,4, -4, -2, -1,1,1 ]))


