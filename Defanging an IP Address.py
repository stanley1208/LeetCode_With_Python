class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".","[.]")

sol=Solution().defangIPaddr("1.1.1.1")
print(sol)

sol=Solution().defangIPaddr("255.100.50.0")
print(sol)