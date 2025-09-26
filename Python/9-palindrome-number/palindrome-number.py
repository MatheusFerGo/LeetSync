class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if x < 0:
            return False
        else:
            return s == s[::-1]