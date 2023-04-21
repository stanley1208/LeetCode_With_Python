class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        toBin=bin(n)
        return toBin.count('1')

sol=Solution().hammingWeight(1101)
print(sol)



