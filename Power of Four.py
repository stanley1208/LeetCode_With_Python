import math
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n>0 and math.log(n,4).is_integer():
            return True
        else:
            return False



sol=Solution().isPowerOfFour(16)
print(sol)