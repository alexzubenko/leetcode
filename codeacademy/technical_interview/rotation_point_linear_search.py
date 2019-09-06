"""
Write a function count_rotations() which has one parameter rotated_list.

count_rotations() should return the index where the sorted list would begin.


rotated_list = ['c', 'd', 'e', 'f', 'a']
rotation_point(rotated_list)
# index 4
# a sorted list would start with 'a'

another_rotated_list = [13, 8, 9, 10, 11]
rotation_point(rotated_list)
# index 1
# a sorted list would start with 8


"""


class Solution:
    # This solution is O(n) because we are using linear search
    # in other words we are visiting each element in the list
    # to find the rotation point
    def rotation_point(self, rotated_list):
        rotation_index = 0
        for i in range(len(rotated_list)-1):
            if rotated_list[i] > rotated_list[i+1]:
                rotation_index = i + 1
        return rotation_index




sol = Solution()
print("Starting testing of our solution \n")

print("{} should = {} \nif input is: {} ===> {}\n".format(sol.rotation_point(
    ['a', 'b', 'c', 'd', 'e', 'f']), 0, ['a', 'b', 'c', 'd', 'e', 'f'],
    0 == sol.rotation_point(['a', 'b', 'c', 'd', 'e', 'f'])))

print("{} should = {} \nif input is: {} ===> {}\n".format(sol.rotation_point(
    ['c', 'd', 'e', 'f', 'a']), 4, ['c', 'd', 'e', 'f', 'a'],
    4 == sol.rotation_point(['c', 'd', 'e', 'f', 'a'])))

print("{} should = {} \nif input is: {} ===> {}\n".format(sol.rotation_point(
    [13, 8, 9, 10, 11]), 1, [13, 8, 9, 10, 11],
    1 == sol.rotation_point([13, 8, 9, 10, 11])))