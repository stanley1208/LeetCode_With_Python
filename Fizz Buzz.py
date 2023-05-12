class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        li=[]

        for i in range(1,n+1):
            if i%15==0:
                li.append("FizzBuzz")
            elif i%3==0:
                li.append("Fizz")
            elif i%5==0:
                li.append("Buzz")
            else:
                li.append(str(i))

        return li


sol=Solution().fizzBuzz(15)
print(sol)
