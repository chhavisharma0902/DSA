class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """

        n = len(accounts)
        sum = 0
        max = 0
        for i in range(n):
            for j in range(len(accounts[i])):
                sum = sum + accounts[i][j]
            if sum > max :
                max = sum
            sum = 0
        return max

        