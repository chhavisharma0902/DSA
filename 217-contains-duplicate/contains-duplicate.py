class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        hash_map = {}
        for i in range(n):
            hash_map[nums[i]] = hash_map.get(nums[i],0)+1
            if (hash_map[nums[i]] > 1):
                return True
        return False