class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        x=str(x)
        str1=x
        str2=''.join(reversed(str1))

        if str1==str2:
            return True
        else:
            return False

sol=Solution().isPalindrome(10)
print(sol)
