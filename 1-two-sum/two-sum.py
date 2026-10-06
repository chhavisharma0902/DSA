class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        h = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in h:
                return [h[complement],i]
            h[num] = i



        
        