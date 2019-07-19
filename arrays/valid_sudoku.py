"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true


Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.


"""

class Solution(object):
    def check_dict (self, diktik):
        for key in diktik.keys():
            if diktik[key] == 1:
                return True

    def subBox (self, board, check, i, j):
        if board[i][j] != "." and board[i][j] in check:
            # print('got one')
            # print(board[i][j])
            # print('got one')
            check[board[i][j]] = 1
        elif board[i][j] != "." and board[i][j] not in check:
            # print('got one')
            # print(board[i][j])
            # print('got one')
            check[board[i][j]] = 0

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in board:
            checkRow = {}
            for j in i:
                if j != "." and j in checkRow:
                    checkRow[j] = 1
                elif j != "." and j not in checkRow:
                    checkRow[j] = 0
            # print(checkRow)
            if self.check_dict(checkRow):
                return False

        for i in range(0,9):
            checkColumn = {}
            for j in board:
                if j[i] != "." and j[i] in checkColumn:
                    checkColumn[j[i]] = 1
                elif j[i] != "." and j[i] not in checkColumn:
                    checkColumn[j[i]] = 0
                if self.check_dict(checkColumn):
                    return False
        checkSubBox = {}
        for i in range(3):
            for j in range(3):
                self.subBox(board,checkSubBox, i, j)
        print(checkSubBox)
        if self.check_dict(checkSubBox):
           return False

        checkSubBox = {}
        for i in range(3):
            for j in range(3,6):
                self.subBox(board, checkSubBox, i, j)
        print(checkSubBox)
        if self.check_dict(checkSubBox):
            return False

        checkSubBox = {}
        for i in range(3):
            for j in range(6,9):
                self.subBox(board, checkSubBox, i, j)
        print(checkSubBox)
        if self.check_dict(checkSubBox):
            return False

        checkSubBox = {}
        for i in range(3,6):
            for j in range(3):
                self.subBox(board, checkSubBox, i, j)
        print(checkSubBox)
        if self.check_dict(checkSubBox):
            return False

        checkSubBox = {}
        for i in range(3, 6):
            for j in range(3,6):
                self.subBox(board, checkSubBox, i, j)
        print(checkSubBox)
        if self.check_dict(checkSubBox):
            return False

        checkSubBox = {}
        for i in range(3, 6):
            for j in range(6, 9):
                self.subBox(board, checkSubBox, i, j)
        print(checkSubBox)
        if self.check_dict(checkSubBox):
            return False

        checkSubBox = {}
        for i in range(6, 9):
            for j in range(3):
                self.subBox(board, checkSubBox, i, j)
        print(checkSubBox)
        if self.check_dict(checkSubBox):
            return False

        checkSubBox = {}
        for i in range(6, 9):
            for j in range(3,6):
                self.subBox(board, checkSubBox, i, j)
        print(checkSubBox)
        if self.check_dict(checkSubBox):
            return False

        checkSubBox = {}
        for i in range(6, 9):
            for j in range(6, 9):
                self.subBox(board, checkSubBox, i, j)
        print(checkSubBox)
        if self.check_dict(checkSubBox):
            return False
        return True




solution = Solution()
# board = [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# print(board[0][4])
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(solution.isValidSudoku(board))
