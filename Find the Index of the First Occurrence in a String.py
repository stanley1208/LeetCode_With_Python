class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            index=haystack.index(needle)
            return index
        else:
            return -1


sol=Solution().strStr("leetcode","leeto")
print(sol)