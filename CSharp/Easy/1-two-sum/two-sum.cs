public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> map = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++){
            int  complement_number = target - nums[i];

            if (map.ContainsKey(complement_number)){
                return new int[] {map[complement_number], i};
            }

            if (!map.ContainsKey(nums[i])){
                map.Add(nums[i], i);
            }
        }
        return new int[0];
    }
}