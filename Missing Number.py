class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(1,len(nums)+1):
            if i not in nums:
                return i

        return 0


sol=Solution().missingNumber([9,6,4,2,3,5,7,0,1])
print(sol)