# Last updated: 25/09/2025, 08:27:18
class Solution:
    def maxScore(self, s: str) -> int:
        # Conta o total de '1' na string inteira (vai ser o valor inicial do lado direito)
        total_ones = s.count('1')
        
        max_score = 0
        left_zeros = 0
        right_ones = total_ones
        
        # Percorre at� o pen�ltimo caractere (divis�o deve deixar os dois lados n�o-vazios)
        for i in range(len(s) - 1):
            if s[i] == '0':
                left_zeros += 1
            else:
                right_ones -= 1
            
            score = left_zeros + right_ones
            max_score = max(max_score, score)
        
        return max_score