# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left,right=self.minDepth(root.left),self.minDepth(root.right)

        if root.left is None and root.right is None:
            return 1

        if root.left is None:
            return 1+right

        if root.right is None:
            return 1+left

        return min(left,right)+1






