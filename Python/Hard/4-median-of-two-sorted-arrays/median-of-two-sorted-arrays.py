class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = nums1 + nums2

        merged_list.sort()

        total_len = len(merged_list)
        mid_index = total_len // 2

        if total_len % 2 == 1:
            return float(merged_list[mid_index])
        else:
            median = (merged_list[mid_index - 1] + merged_list[mid_index]) / 2
            return median