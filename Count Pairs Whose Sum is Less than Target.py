class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sum=0
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if i<j and nums[i]+nums[j]<target:
                    sum+=1
        return sum

sol=Solution().countPairs([-1,1,2,3,1],2)
print(sol)

sol=Solution().countPairs([-6,2,5,-2,-7,-1,3],-2)
print(sol)