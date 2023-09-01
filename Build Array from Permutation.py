class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        li=[]
        for i in range(0,len(nums)):
            li.append(nums[nums[i]])
        return li

sol=Solution().buildArray([0,2,1,5,3,4])
print(sol)

sol=Solution().buildArray([5,0,1,2,3,4])
print(sol)