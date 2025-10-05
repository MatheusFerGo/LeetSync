class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total_len = m + n
        
        i, j = 0, 0
        
        m1, m2 = 0, 0
        
        for count in range((total_len // 2) + 1):
            m1 = m2
            
            if i < m and (j >= n or nums1[i] <= nums2[j]):
                m2 = nums1[i]
                i += 1
            elif j < n:
                m2 = nums2[j]
                j += 1

        if total_len % 2 == 1:
            return float(m2)
        else:
            return (m1 + m2) / 2.0