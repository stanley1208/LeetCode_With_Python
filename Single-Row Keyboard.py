class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        sum=0
        position=keyboard[0]
        for i in word:
            sum+=abs(keyboard.index(i)-keyboard.index(position))
            position=i
        return sum

sol=Solution().calculateTime("abcdefghijklmnopqrstuvwxyz","cba")
print(sol)

sol=Solution().calculateTime("pqrstuvwxyzabcdefghijklmno","leetcode")
print(sol)