class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        li=[]
        for i in range(n):
            li.append(nums[i])
            li.append(nums[i+n])

        return li

sol=Solution().shuffle([1,1,2,2],2)
print(sol)