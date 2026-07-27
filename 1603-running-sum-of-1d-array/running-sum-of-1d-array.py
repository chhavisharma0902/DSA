class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        total =0
        for i in range(len(nums)-1,-1,-1):
            total = sum(nums[0:i+1])
            res[i]=total

        return res
        