import numpy as np
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
            return False

        return np.floor(np.log2(n)) == np.ceil(np.log2(n))



sol=Solution().isPowerOfTwo(536870912)
print(sol)