class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d={}
        for i in range(len(nums)):
            if nums[i] in d and i-d[nums[i]]<=k:
                return True
            d[nums[i]]=i
        return False

sol=Solution().containsNearbyDuplicate([1,2,3,1],3)
print(sol)
