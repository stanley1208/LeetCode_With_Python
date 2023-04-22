class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        character=""

        while columnNumber>0:

            columnNumber=columnNumber-1

            character=chr((columnNumber%26)+65)+character

            columnNumber=columnNumber//26

        return character





sol=Solution().convertToTitle(1)
print(sol)

sol=Solution().convertToTitle(28)
print(sol)

sol=Solution().convertToTitle(701)
print(sol)