"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place,
which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]


"""

class Solution(object):
    # the below solution works for clockwise:
    # reverse, then transpose
    # for anticlockwise we should do:
    # transpose, then reverse
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        print('Initial array')
        for i in matrix:
            print(i)
        # Reverse initial array to simplify the solution:
        # matrix.reverse()

        # matrix reverse
        for i in range(len(matrix)):
            for j in range(len(matrix)-1):
                k = len(matrix) -1 -j
                matrix[j][i], matrix[k][i] = matrix[k][i],matrix[j][i]
        print('Reversed array')
        for i in matrix:
            print(i)

        # matrix transpose
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print('Rotated array')
        for i in matrix:
            print(i)
        return matrix



solution = Solution()
print(solution.rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
]))
# print(solution.rotate([
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ]))