// Last updated: 25/09/2025, 08:27:11
public class Solution {
    public bool MakeEqual(string[] words) {
        int n = words.Length;
        int[] freq = new int[26];

        foreach (var word in words){
            foreach (var c in word) {
                freq[c - 'a']++;
            }
        }

        foreach (var count in freq) {
            if (count % n != 0) return false;
        }
        return true;
    }
}