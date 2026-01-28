class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_map = {}

        for i, n in enumerate(nums):
            complement_number = target - n

            if complement_number in previous_map:
                return [previous_map[complement_number], i]

            previous_map[n] = i

        return []