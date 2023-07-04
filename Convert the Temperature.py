class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        li=[]
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        li.append(Kelvin)
        li.append(Fahrenheit)
        return li

sol=Solution().convertTemperature(0)
print(sol)