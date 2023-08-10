class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        li=[]
        for i in range(len(accounts)):
            li.append(sum(accounts[i]))

        return max(li)

sol=Solution().maximumWealth([[1,2,3],[3,2,1]])
print(sol)

sol=Solution().maximumWealth([[1,5],[7,3],[3,5]])
print(sol)

sol=Solution().maximumWealth([[2,8,7],[7,1,3],[1,9,5]])
print(sol)