class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]


sol=Solution().majorityElement([3,2,3])
print(sol)

sol=Solution().majorityElement([2,2,1,1,1,2,2])
print(sol)

