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
            if nums[i]%2!=0:
                temp = nums[j]
                nums[j]=nums[i]
                nums[i]=temp
                j -=1
            else:
                i+=1
        return nums
