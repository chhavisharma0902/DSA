class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)

        temp = 0
        while x != 0:
            y = x % 10
            temp = (temp * 10) + y
            x = x//10

        temp = temp * sign

        if temp < -2147483648 or temp > 2147483647:
            return 0
        return temp