class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and i<j:
                    count+=1
        return count

sol=Solution().numIdenticalPairs([1,2,3,1,1,3])
print(sol)

sol=Solution().numIdenticalPairs([1,1,1,1])
print(sol)

sol=Solution().numIdenticalPairs([1,2,3])
print(sol)