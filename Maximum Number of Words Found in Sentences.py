class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        li=[]
        for i in range(len(sentences)):
            sentences[i]=sentences[i].split()
            li.append(len(sentences[i]))

        return max(li)


sol=Solution().mostWordsFound(["alice and bob love leetcode","i think so too","this is great thanks very much"])
print(sol)

sol=Solution().mostWordsFound(["please wait","continue to fight","continue to win"])
print(sol)