class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_chars_map = {}
        t_chars_map = {}

        for char in s:
            if char in s_chars_map:
                s_chars_map[char] += 1
            else:
                s_chars_map[char] = 1
            
        for char in t:
            if char in t_chars_map:
                t_chars_map[char] += 1
            else:
                t_chars_map[char] = 1

        return s_chars_map == t_chars_map