class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:

                i = max(mp[s[j]], i)
                print(mp[s[j]])
            ans = max(ans, j - i + 1)
            print(ans)
            mp[s[j]] = j + 1


        return ans

sol=Solution().lengthOfLongestSubstring("pwwkew")
print(sol)