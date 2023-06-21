class Solution(object):
    def removeVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel='aeiou'
        for i in s:
            if i in vowel:
                s=s.replace(i,"")

        return s

sol=Solution().removeVowels("leetcodeisacommunityforcoders")
print(sol)
