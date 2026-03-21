class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_map = {}
        
        for char in s:
            count_map[char] = count_map.get(char, 0) + 1
            
        for char in t:
            if char not in count_map or count_map[char] == 0:
                return False
            count_map[char] -= 1
            
        return True