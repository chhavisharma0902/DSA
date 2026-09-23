class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        temp = 0
        j = n - 1
        i = 0
        while(i<j):
            if nums[i]%2==0:
                i +=1
            else:
                nums[i],nums[j] = nums[j],nums[i]
                j -=1
        return nums
