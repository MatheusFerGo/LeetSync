class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []
        bracket_map = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in bracket_map:
                if len(bracket_stack) == 0 or bracket_stack.pop() !=  bracket_map[char]:
                    return False
                
            else:
                bracket_stack.append(char)
        
        return not bracket_stack