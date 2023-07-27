class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        li=[]
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            li.append(sum)

        return li

sol=Solution().runningSum([1,2,3,4])
print(sol)

sol=Solution().runningSum([1,1,1,1,1])
print(sol)

sol=Solution().runningSum([3,1,2,10,1])
print(sol)
