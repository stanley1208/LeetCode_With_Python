class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel='aeiouAEIOU'
        s=list(s)
        front,end=0,len(s)-1

        while front<end:
            if s[front] in vowel and s[end] in vowel:
                s[front],s[end]=s[end],s[front]
                front+=1
                end-=1
            elif s[front] not in vowel:
                front+=1
            elif s[end] not in vowel:
                end-=1

        return "".join(s)






sol=Solution().reverseVowels('stanley')
print(sol)