class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numsToSet=set(nums)
        numsToList=list(numsToSet)
        if len(nums)==len(numsToList):
            return False
        else:
            return True


sol=Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2])
print(sol)