class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=''
        m=map(str,digits)
        d=(int(s.join(m))+1)
        li=list(map(int,list(str(d))))

        return li



sol=Solution().plusOne([1,2,3])
print(sol)