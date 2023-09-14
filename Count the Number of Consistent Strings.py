class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        sum=0
        for i in words:
            if set(i)<=set(allowed):
                sum+=1

        return sum

sol=Solution().countConsistentStrings("ab",["ad","bd","aaab","baa","badab"])
print(sol)

sol=Solution().countConsistentStrings("abc",["a","b","c","ab","ac","bc","abc"])
print(sol)

sol=Solution().countConsistentStrings("cad",["cc","acd","b","ba","bac","bad","ac","d"])
print(sol)