"""

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# https://www.youtube.com/watch?v=azupT01iC78
class Solution(object):
    # default values here is fot recursion calls
    # for the first call we have no parent nodes
    def isValidBST(self, root, min=-100000000, max=1000000000000):
    # if you use python3 and have access to sys module you can import it
    # and do the following
    # def isValidBST(self, root, min=-sys.maxint, max=sys.maxint):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        # in this base case we are checking if the current node
        # sattisfy the criterias of the binary search tree
        # then in recursion calls max for the left child
        # would be the parent node value and for
        # the right child min would be parent node value
        if root.val > min and root.val < max\
            and self.isValidBST(root.left, min, root.val)\
            and self.isValidBST(root.right, root.val, max):
            return True
        # if any from the above is fail, we return Fasle
        else:
            return False


        # if not root:
        #     return True
        # if root and root.left and root.right:
        #     if root.left.val < root.val and root.right.val > root.val:
        #         return True
        #     self.isValidBST(root.left)
        #     self.isValidBST(root.right)
        # return False



# Driver code
root = TreeNode(1)
root.left = TreeNode(-1)
# root.right = TreeNode(25)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(10)
# root.right.left = TreeNode(3)
# root.right.right = TreeNode(40)
# root.right.right.left = TreeNode(8)
# root.right.right.left.right = TreeNode(9)
solution = Solution()
print(solution.isValidBST(root))