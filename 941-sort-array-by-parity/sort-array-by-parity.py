class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        if n<=1:
            return nums

        temp = 0
        start = 0

        for i in range(n):
            if nums[i]%2==0:
                temp = nums[start]
                nums[start]=nums[i]
                nums[i]=temp
                start +=1
                i+=1
            else:
                i+=1
        return nums
