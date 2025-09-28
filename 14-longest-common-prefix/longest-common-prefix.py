class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        strs.sort()
        first_word = strs[0]
        last_word = strs[-1]
        i = 0

        while i < len(first_word) and i < len(last_word) and first_word[i] == last_word[i]:
            i += 1

        return first_word[:i]