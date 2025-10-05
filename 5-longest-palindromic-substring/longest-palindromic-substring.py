class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, end = 0, 0

        for i in range(len(s)):
            len1 = self._expand_around_center(s, i, i)

            len2 = self._expand_around_center(s, i, i+1)

            length = max(len1, len2)

            if length > end - start:
                start = i - (length - 1 )//2
                end = i + length // 2
            
        return s[start : end + 1]

    def _expand_around_center(self, s:str, left:int, right:int) -> int:
        L,R = left, right

        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1

        return R - L - 1