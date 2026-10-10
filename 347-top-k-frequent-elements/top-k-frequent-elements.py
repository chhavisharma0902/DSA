class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash_map = {}
        res = []
        for i in range(len(nums)):
            hash_map[nums[i]]=hash_map.get(nums[i],0) + 1

        sorted_by_val = sorted(hash_map.items(), key=lambda item: item[1], reverse = True)

        for i in range(k):
            res.append(sorted_by_val[i][0])
        
        return res