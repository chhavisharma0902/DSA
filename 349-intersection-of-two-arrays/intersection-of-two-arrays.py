class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        res = set()
        m = len(nums1)
        n = len(nums2) 
        i = 0
        j = 0
        while i<m and j<n:
            if(nums1[i]==nums2[j]):
                res.add(nums1[i])
                i+=1
                j+=1
            elif(nums1[i]>nums2[j]):
                j+=1
            else:
                i+=1
            
        return list(res)