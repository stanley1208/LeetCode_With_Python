class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        indices1 = [i for i, x in enumerate(wordsDict) if x == word1]

        indices2 = [i for i, x in enumerate(wordsDict) if x == word2]

        distance=[]

        for i in indices1:
            for j in indices2:
                distance.append(abs(i-j))


        return min(distance)


sol=Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice")
print(sol)