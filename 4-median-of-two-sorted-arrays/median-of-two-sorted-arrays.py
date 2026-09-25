class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        total_len = m+n
        mid = total_len//2
        curr_val = 0
        prev_val = 0
        i = 0
        j = 0

        for _ in range(mid+1):
            prev_val = curr_val

            if i<m and (j>=n or nums1[i] <= nums2[j]):
                curr_val = nums1[i]
                i +=1
            else:
                curr_val = nums2[j]
                j +=1
            
        if(total_len % 2==0):
            return (prev_val + curr_val) / 2.0
        else:
            return float(curr_val)
        

        