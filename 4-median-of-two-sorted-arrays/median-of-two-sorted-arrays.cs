public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.Length;
        int n = nums2.Length;
        int totalLength = m + n;

        if (totalLength == 0) {
            return 0.0;
        }

        int i = 0, j = 0;
        int m1 = 0, m2 = 0;

        for (int count = 0; count <= totalLength / 2; count++) {
            m1 = m2;

            bool isNums1Exhausted = i >= m;
            bool isNums2Exhausted = j >= n;

            if (!isNums1Exhausted && !isNums2Exhausted) {
                if (nums1[i] <= nums2[j]) {
                    m2 = nums1[i];
                    i++;
                } else {
                    m2 = nums2[j];
                    j++;
                }
            } 
            else if (!isNums1Exhausted) {
                m2 = nums1[i];
                i++;
            } 
            else if (!isNums2Exhausted) {
                m2 = nums2[j];
                j++;
            }
        }

        if (totalLength % 2 == 1) {
            return (double)m2;
        } else {
            return (m1 + m2) / 2.0;
        }
    }
}