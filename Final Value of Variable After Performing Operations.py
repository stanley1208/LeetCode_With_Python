class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        X=0
        for i in operations:
            if i=="X++" or i=="++X":
                X+=1
            elif i=="X--" or i=="--X":
                X-=1

        return X

sol=Solution().finalValueAfterOperations(["X++","++X","--X","X--"])
print(sol)