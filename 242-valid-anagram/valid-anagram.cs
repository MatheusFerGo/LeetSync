public class Solution {
    public bool IsAnagram(string s, string t) {
        if(s.Length != t.Length) return false;

        int[] charCounts = new int[26];

        for (int i = 0; i < s.Length; i++){
            charCounts[s[i] - 'a']++;
            charCounts[t[i] - 'a']--;
        }

        foreach (int count in charCounts){
            if(count != 0) return false;
        }

        return true;
    }
}