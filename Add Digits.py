class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        sum=0
        string=str(num)
        for i in string:
            i=int(i)
            sum+=i

        if len(str(sum)) == 1:
            return sum
        else:
            return self.addDigits(sum)






sol=Solution().addDigits(38)
print(sol)