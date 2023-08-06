class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n%2==0:
            return n
        else:
            return 2*n

sol=Solution().smallestEvenMultiple(5)
print(sol)

sol=Solution().smallestEvenMultiple(6)
print(sol)

