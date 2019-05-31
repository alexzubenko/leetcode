"""

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

"""
import sys

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    # https://www.youtube.com/watch?v=6oL-0TdVy28

    def preorded_count(self, startpoint, count=0):
        if startpoint:
            count +=1
            count += self.preorded_count(startpoint.left)
            # count += self.preorded_count(startpoint.right)
        return count


    # preorder
    # root --> left --> right
    def preorded(self, startpoint):
        if startpoint:
            print(str(startpoint.val) + '--')
            self.preorded(startpoint.left)
            self.preorded(startpoint.right)

    # inorder
    # left --> root --> right
    def inorder(self, startpoint):
        if startpoint:

            self.preorded(startpoint.left)
            print(str(startpoint.val) + '--')
            self.preorded(startpoint.right)

    # postorder
    # left --> right --> root
    def postorder(self, startpoint):
        if startpoint:

            self.preorded(startpoint.left)
            self.preorded(startpoint.right)
            print(str(startpoint.val) + '--')


    # def print_tree(self, startpoint, result = ''):
    #         if startpoint:
    #             result += str(startpoint.val) + " -  "
    #             result = self.print_tree(startpoint.left, result)
    #             result = self.print_tree(startpoint.right, result)
    #         return result
    #
    # def print_tree_simple(self, startpoint):
    #         if startpoint:
    #             print(str(startpoint.val) + " -  "),
    #             self.print_tree_simple(startpoint.left)
    #             self.print_tree_simple(startpoint.right)
    #
    # def print_tree_count(self, startpoint, count=0):
    #     if startpoint:
    #         count+=1
    #         print(str(startpoint.val) + " - "),
    #         self.print_tree(startpoint.left, count)
    #         self.print_tree(startpoint.right, count)
    #     return count
    #
    #
    #
    # def print_tree_inorder(self,root):
    #     if root:
    #         self.print_tree_inorder(root.left)
    #         print(root.val),
    #         self.print_tree_inorder(root.right)
    #
    # def printpostorder(self, root):
    #     if root:
    #         self.printpostorder(root.left)
    #         self.printpostorder(root.right)
    #         print(root.val),
    # def printpreorder(self, root):
    #     if root:
    #         print(root.val),
    #         self.printpreorder(root.left)
    #         self.printpreorder(root.right)

    # https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        else:
            leftMax = self.maxDepth(root.left)
            rightMax = self.maxDepth(root.right)

            if leftMax > rightMax:
                return leftMax + 1
            else:
                return rightMax + 1




# Driver code
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(8)
root.right.right.left.right = TreeNode(9)
solution = Solution()
print(solution.maxDepthMath(root))