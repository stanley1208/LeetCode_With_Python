# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        total=len(nums)
        if not total:
            return None


        middle=total//2

        root = TreeNode(nums[middle])

        root.left=self.sortedArrayToBST(nums[:middle])

        root.right=self.sortedArrayToBST(nums[middle+1:])

        return root

sol=Solution().sortedArrayToBST([-10,-3,0,5,9])
print(sol.val)