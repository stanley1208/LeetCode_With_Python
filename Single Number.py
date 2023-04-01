class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        for i in range(len(nums)):
            if nums.count(nums[i])==1:
                return nums[i]

sol=Solution().singleNumber([2,2,1])
print(sol)

sol=Solution().singleNumber([4,1,2,1,2])
print(sol)

sol=Solution().singleNumber([1])
print(sol)