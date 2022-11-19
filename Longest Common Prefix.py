class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        a=""
        prefix = []
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
        return a.join(prefix)

sol=Solution().longestCommonPrefix(["flower","flow","flight"])
print(sol)





