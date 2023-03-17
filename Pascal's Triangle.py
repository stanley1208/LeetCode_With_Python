class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        [[1],
         [1,1],
         [1,2,1],
         [1,3,3,1],
         [1,4,6,4,1]
        ]
        """
        p=[[1]*(i+1) for i in range(numRows)]

        for i in range(numRows):
            for j in range(1,i):
                p[i][j]=p[i-1][j-1]+p[i-1][j]

        return p

sol=Solution().generate(10)
print(sol)

