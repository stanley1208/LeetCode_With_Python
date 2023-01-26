# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.isSameTree(root.left,root.right)

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if not p and not q:
            return True


        if p and q and p.val==q.val:
            return self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)

        return False

