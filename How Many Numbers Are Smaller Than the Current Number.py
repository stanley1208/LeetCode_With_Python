class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        li=[]
        for i in nums:
            count=0
            for j in nums:
                if j<i:
                   count+=1
            li.append(count)
        return li

sol=Solution().smallerNumbersThanCurrent([8,1,2,2,3])
print(sol)

sol=Solution().smallerNumbersThanCurrent([6,5,4,8])
print(sol)

sol=Solution().smallerNumbersThanCurrent([7,7,7,7])
print(sol)