class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        
        def solve(i,j):
            if (i,j) in memo:
                return memo[(i,j)]

            if j == len(p):
                return i == len(s)

            first_match = (i < len(s) and (p[j] == s[i] or p[j] == '.'))

            if j + 1 < len(p) and p[j+1] == '*':
                ignore_pattern = solve(i,j+2)

                use_pattern = first_match and solve(i+1,j)

                result = ignore_pattern or use_pattern
            else:
                result = first_match and solve(i+1,j+1)

            memo[(i,j)] = result
            return result

        return solve(0,0)