# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and q:
            return False

        elif p and not q:
            return False

        elif not p and not q:
            return True

        elif p.val!=q.val:
            return False

        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)




