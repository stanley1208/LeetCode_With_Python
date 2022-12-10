class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        s=s.strip()
        count=0
        for i in range(0,len(s)):
            if s[i].isspace():
                count=0
            else:
                count+=1

        return count


sol=Solution().lengthOfLastWord("luffy is still joyboy")
print(sol)