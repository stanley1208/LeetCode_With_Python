class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        return command.replace("()","o").replace("(al)","al")

sol=Solution().interpret("G()(al)")
print(sol)

sol=Solution().interpret("G()()()()(al)")
print(sol)

sol=Solution().interpret("(al)G(al)()()G")
print(sol)