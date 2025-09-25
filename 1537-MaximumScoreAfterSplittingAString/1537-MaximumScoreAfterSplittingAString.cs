// Last updated: 25/09/2025, 08:27:16
public class Solution {
    public int MaxScore(string s) {
        int totalOnes = 0;
        foreach (char c in s) {
            if (c == '1') totalOnes++;
        }

        int maxScore = 0;
        int leftZeros = 0;
        int rightOnes = totalOnes;

        // percorre at� o pen�ltimo caractere
        for (int i = 0; i < s.Length - 1; i++) {
            if (s[i] == '0') {
                leftZeros++;
            } else {
                rightOnes--;
            }

            int score = leftZeros + rightOnes;
            if (score > maxScore) {
                maxScore = score;
            }
        }

        return maxScore;
    }
}