class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        count=0
        for i in hours:
            if i>=target:
                count+=1

        return count

sol=Solution().numberOfEmployeesWhoMetTarget([0,1,2,3,4],2)
print(sol)

sol=Solution().numberOfEmployeesWhoMetTarget([5,1,4,2,2],6)
print(sol)