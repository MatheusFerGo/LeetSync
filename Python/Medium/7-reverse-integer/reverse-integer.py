class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1

        sign = 1 if x >= 0 else -1
        num_str = str(abs(x))
        reversed_str = num_str[::-1]
        reversed_int = int(reversed_str) * sign

        if not (MIN_INT <= reversed_int <= MAX_INT):
            return 0

        return reversed_int