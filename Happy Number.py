class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=[]
        while n!=1:
            if n in s:
                return False
            s.append(n)
            # print(s)
            n=sum(int(i)**2 for i in str(n))

        return True


sol=Solution().isHappy(2)
print(sol)