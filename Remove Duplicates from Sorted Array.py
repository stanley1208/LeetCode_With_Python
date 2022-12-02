class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index=0
        for i in range(1,len(nums)):
            if nums[i] !=nums[index]:
                index+=1
                nums[index]=nums[i]

        return index+1,nums


sol=Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(sol)


