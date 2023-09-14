class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sum=0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i==j or i+j==(len(mat[i])-1):
                    sum+=mat[i][j]

        return sum

sol=Solution().diagonalSum([[1,2,3],[4,5,6],[7,8,9]])
print(sol)

sol=Solution().diagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]])
print(sol)

sol=Solution().diagonalSum([[5]])
print(sol)