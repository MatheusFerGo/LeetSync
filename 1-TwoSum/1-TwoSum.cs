// Last updated: 25/09/2025, 08:27:22
using System;
using System.Collections.Generic;

public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> numMap = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++) {
            int complement = target - nums[i];

            if (numMap.ContainsKey(complement)) {
                return new int[] { numMap[complement], i };
            }

            numMap[nums[i]] = i;
        }

        return new int[0];
    }
}
