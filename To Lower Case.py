class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.lower()
        return s

sol=Solution().toLowerCase("Hello")
print(sol)

sol=Solution().toLowerCase("here")
print(sol)

sol=Solution().toLowerCase("LOVELY")
print(sol)