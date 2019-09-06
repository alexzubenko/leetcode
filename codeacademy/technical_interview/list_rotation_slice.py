"""
rotate the list like:

list = ['a', 'b', 'c', 'd', 'e', 'f']
rotate(list, 0)
# ['a', 'b', 'c', 'd', 'e', 'f']
rotate(list, 1)
# ['f', 'a', 'b', 'c', 'd', 'e']
rotate(list, 3)
# ['d', 'e', 'f', 'a', 'b', 'c']

"""

class Solution:
    # This solution has the following complexity:
    # Memory: O(1) - we transforming array in place and do not crate anything new
    # Time: O(n) - we need to visit num_rotations elements in the array,
    # we can represent it as a "n" therefore we have O(n)
    def rotate(self, lst, num_rotations):
        if num_rotations == 0 or len(lst) == num_rotations:
            return lst
        while num_rotations:
            lst.insert(0, lst.pop())
            num_rotations -=1
        return lst

    # This solution has the following complexity:
    # Memory: O(1) - we transforming array in place and do not crate anything new
    # Time: O(n) - we need to run the recursion function in worse case for each element
    # therefore we have O(n)
    # Recursion solution
    def rotate_recutsion(self, lst, num_rotation):
        # this is the base case if it is True we are done here
        if num_rotation < 1:
            return lst
        # doing what needs to be done because base case
        # is still not true
        lst.insert(0, lst.pop())
        # After we did main part we should invoke the function again
        # but this time we will decrease the number of rotations by 1
        # and we will do it again and again as long as base case is
        # not true
        return self.rotate(lst, num_rotation-1)

    # Slice operator solution
    # This solution has the following complexity:
    # Memory: O(n) - we creating new array
    # Time: O(1) - we dont need to visit each element
    def rotate_slice(self, lst, num_rotations):
        return lst[-num_rotations:] + lst[:-num_rotations]




# Test cases:
sol = Solution()
print("The {} should transform to {} and the result is {}".format(
['a', 'b', 'c', 'd', 'e', 'f'], sol.rotate(['a', 'b', 'c', 'd', 'e', 'f'], 0),
    ['a', 'b', 'c', 'd', 'e', 'f'] == sol.rotate(['a', 'b', 'c', 'd', 'e', 'f'],0)
))

print("The {} should transform to {} and the result is {}".format(
['a', 'b', 'c', 'd', 'e', 'f'], sol.rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1),
    ['f', 'a', 'b', 'c', 'd', 'e'] == sol.rotate(['a', 'b', 'c', 'd', 'e', 'f'],1)
))

print("The {} should transform to {} and the result is {}".format(
['a', 'b', 'c', 'd', 'e', 'f'], sol.rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3),
    ['d', 'e', 'f', 'a', 'b', 'c'] == sol.rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3)
))
#-------------------------------------------------------------------
print("Starting tests for Recursion implementation!!!")

print("The {} should transform to {} and the result is {}".format(
['a', 'b', 'c', 'd', 'e', 'f'], sol.rotate_recutsion(['a', 'b', 'c', 'd', 'e', 'f'], 0),
    ['a', 'b', 'c', 'd', 'e', 'f'] == sol.rotate_recutsion(['a', 'b', 'c', 'd', 'e', 'f'],0)
))

print("The {} should transform to {} and the result is {}".format(
['a', 'b', 'c', 'd', 'e', 'f'], sol.rotate_recutsion(['a', 'b', 'c', 'd', 'e', 'f'], 1),
    ['f', 'a', 'b', 'c', 'd', 'e'] == sol.rotate_recutsion(['a', 'b', 'c', 'd', 'e', 'f'],1)
))

print("The {} should transform to {} and the result is {}".format(
['a', 'b', 'c', 'd', 'e', 'f'], sol.rotate_recutsion(['a', 'b', 'c', 'd', 'e', 'f'], 3),
    ['d', 'e', 'f', 'a', 'b', 'c'] == sol.rotate_recutsion(['a', 'b', 'c', 'd', 'e', 'f'], 3)
))

#------------------------------------------------

print('Starting Tests for slice solution')
print("The {} should transform to {} and the result is {}".format(
['a', 'b', 'c', 'd', 'e', 'f'], sol.rotate_slice(['a', 'b', 'c', 'd', 'e', 'f'], 0),
    ['a', 'b', 'c', 'd', 'e', 'f'] == sol.rotate_slice(['a', 'b', 'c', 'd', 'e', 'f'],0)
))

print("The {} should transform to {} and the result is {}".format(
['a', 'b', 'c', 'd', 'e', 'f'], sol.rotate_slice(['a', 'b', 'c', 'd', 'e', 'f'], 1),
    ['f', 'a', 'b', 'c', 'd', 'e'] == sol.rotate_slice(['a', 'b', 'c', 'd', 'e', 'f'],1)
))

print("The {} should transform to {} and the result is {}".format(
['a', 'b', 'c', 'd', 'e', 'f'], sol.rotate_slice(['a', 'b', 'c', 'd', 'e', 'f'], 3),
    ['d', 'e', 'f', 'a', 'b', 'c'] == sol.rotate_slice(['a', 'b', 'c', 'd', 'e', 'f'], 3)
))
