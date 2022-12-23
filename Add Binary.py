class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        base1=int(a,base=2)
        base2=int(b,base=2)

        total=base1+base2


        return format(total,"b")

sol=Solution().addBinary("1010","1011")
print(sol)
