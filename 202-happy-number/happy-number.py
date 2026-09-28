class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digit = 0 
        while True:
            ans = 0

            while n>0:
                digit = n % 10
                ans = ans + (digit**2)
                n = n // 10

            if(ans == 4):
                return False

            if(ans == 1):
               return True

            n = ans