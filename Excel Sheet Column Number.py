class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        total=0
        for i in range(len(columnTitle)):
            total=total*26+(ord(columnTitle[i])-ord("A"))+1
        return total



sol=Solution().titleToNumber("AA")
print(sol)

sol=Solution().titleToNumber("B")
print(sol)

sol=Solution().titleToNumber("C")
print(sol)