import numpy as np


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minVal=np.inf
        max_profit=0

        for i in range(len(prices)):
            minVal=min(prices[i],minVal)
            max_profit=max(max_profit,prices[i]-minVal)

        if max_profit==0:
            return 0
        else:
            return max_profit










sol=Solution().maxProfit([7,6,4,3,1])
print(sol)



