class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        li=[""]*len(s)
        for i,j in enumerate(indices):
            li[j]=s[i]
        return "".join(li)

sol=Solution().restoreString("codeleet",[4,5,6,7,0,2,1,3])
print(sol)

sol=Solution().restoreString("abc",[0,1,2])
print(sol)
