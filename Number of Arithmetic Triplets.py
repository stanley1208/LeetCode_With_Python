class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        sum=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i<j<k and (nums[j]-nums[i])==diff and (nums[k]-nums[j])==diff:
                        sum+=1
        return sum

sol=Solution().arithmeticTriplets([0,1,4,6,7,10],3)
print(sol)

sol=Solution().arithmeticTriplets([4,5,6,7,8,9],2)
print(sol)