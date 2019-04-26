"""
Given an array nums, write a function to
move all 0's to the end of it while maintaining the
relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.



"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # searchim for the last non zero index
        gi = 0
        for i in range(len(nums)):
            if nums[i] !=0:
                gi = i
        if gi == 0:
            return nums
        print(gi)

        # appending all zeroes to the tails of the nums
        for i in range(gi+1):
            if nums[i] == 0:
                nums.append(nums[i])
        print(nums)

        #  starting from the beginning and removing all zeroes from
        # nums till the last non zero index
        i = 0
        while i < gi:
            print(i)
            print(gi)
            print(nums)
            if nums[i] == 0:
                # please note that nums.pop(i) and nums.remove(i)
                # are not the same, pop will delete by index and remove
                # will delete by order
                # example:
                # [1,2,3,4,5]
                # nums.pop(1) = [1,3,4,5]
                # nums.remove(1) = [2,3,4,5]
                nums.pop(i)
                # after poping the element decreasing the last index by 1
                gi -=1
            else:
                # if is not zero, increasing index to strat with
                # the nex element in the next iteration
                i+=1
        return nums



solution = Solution()
# print(solution.moveZeroes([0,1,0,3,12]))
print(solution.moveZeroes([1,0,1]))