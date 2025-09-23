public class Solution {
    public int MaxScore(string s) {
        int totalOnes = 0;
        foreach (char c in s) {
            if (c == '1') totalOnes++;
        }

        int maxScore = 0;
        int leftZeros = 0;
        int rightOnes = totalOnes;

        // percorre até o penúltimo caractere
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