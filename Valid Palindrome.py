class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        special=" !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        s=s.lower()
        s=s.strip()
        # s=s.replace(" ","")
        for i in range(len(special)):
            if special[i] in s:
                s=s.replace(special[i],"")
        rev_s=s[::-1]

        if(s==rev_s):
            return True
        else:
            return False


sol=Solution().isPalindrome("Marge, let's \"[went].\" I await {news} telegram.")
print(sol)

sol=Solution().isPalindrome("race a car")
print(sol)

sol=Solution().isPalindrome(" ")
print(sol)
