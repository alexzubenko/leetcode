"""

Write a function count_rotations() which has one parameter rotated_list.

count_rotations() should return the index where the sorted list would begin.

Your solution should make use of binary search for a O(logN) time complexity!


"""
class Solution:
    # This function should leverage binary search
    # to have time complexity O(logN) instead of linear search O(N)
    def rotation_point(self, rot_list):
        print(rot_list)
        low = 0 # first index of the list
        high = len(rot_list)-1 # last valid index of the list
        # if we do the len(rot_list) - it will cause index out of range error
        while low <= high:
            print('low index is: ', low)
            print('high index is: ', high)
            print(rot_list[low:high+1])
            mid = (low + high)//2
            print('the mid here is: ', mid)
            # The following trick will make sure that indexed will always be valid
            # in other words always in the list indexes range
            # the similar technick is in use in the hash compressor function
            # when we do hash_value % len(array) to ger index
            mid_next = (mid +1) % len(rot_list)
            mid_prev = (mid-1) % len(rot_list)
            # mid_next = (mid +1)
            # mid_prev = (mid-1)
            if rot_list[mid] < rot_list[mid_next] and rot_list[mid] < rot_list[mid_prev]:
                return mid
            elif rot_list[mid]< rot_list[high]:
                print('Our mid is not good enough mid < high, searching in the'
                      ' left part of the list')
                high = mid - 1
                print(rot_list[low:high+1])
            else:
                print('Our mid is not good enough mid > high, searching in the'
                      ' right part of the list')
                low = mid + 1
                print(rot_list[low:high+1])


sol = Solution()
print("Starting testing our solution\n")

print("{} should be = {}\nif "
      "input is: {} and it is ==> {}".format(sol.rotation_point(
       ['c', 'd', 'e', 'f', 'a', 'b']),
        4, ['c', 'd', 'e', 'f', 'a', 'b'], 4
        == sol.rotation_point(['c', 'd', 'e', 'f', 'a', 'b'])))
#
# #
print("{} should be = {}\nif "
      "input is: {} and it is ==> {}".format(sol.rotation_point(
       ['d', 'e', 'f', 'a', 'b', 'c']),
        3,  ['d', 'e', 'f', 'a', 'b', 'c'], 3
        == sol.rotation_point( ['d', 'e', 'f', 'a', 'b', 'c'])))
#
print("{} should be = {}\nif "
      "input is: {} and it is ==> {}".format(sol.rotation_point(
       ['a', 'b', 'c', 'd', 'e', 'f']),
        0,  ['a', 'b', 'c', 'd', 'e', 'f'], 0
        == sol.rotation_point(['a', 'b', 'c', 'd', 'e', 'f'])))
#
print("{} should be = {}\nif "
      "input is: {} and it is ==> {}".format(sol.rotation_point(
    [13, 8, 9, 10, 11]),
        1,  [13, 8, 9, 10, 11], 1
        == sol.rotation_point([13, 8, 9, 10, 11])))

# print(sol.rotation_point([13, 8, 9, 10, 11]))

# print(sol.rotation_point(['d', 'e', 'f', 'a', 'b', 'c']))

# print(sol.rotation_point(['c', 'd', 'e', 'f', 'a']))

