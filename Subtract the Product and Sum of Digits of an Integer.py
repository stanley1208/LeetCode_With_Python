class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        product=1
        sum=0
        for i in str(n):
            product*=int(i)
            sum+=int(i)
        return product-sum

sol=Solution().subtractProductAndSum(234)
print(sol)

sol=Solution().subtractProductAndSum(4421)
print(sol)