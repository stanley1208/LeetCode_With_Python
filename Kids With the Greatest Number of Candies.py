class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        li=[True if (candies[i]+extraCandies)>=max(candies) else False for i in range(0,len(candies))]
        return li

sol=Solution().kidsWithCandies([2,3,5,1,3],3)
print(sol)

sol=Solution().kidsWithCandies([4,2,1,1,2],1)
print(sol)

sol=Solution().kidsWithCandies([12,1,12],10)
print(sol)