public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) return false;

        var counts = new Dictionary<char, int>();

        foreach (char c in s) {
            counts[c] = counts.GetValueOrDefault(c, 0) + 1;
        }

        foreach (char c in t) {
            if (!counts.ContainsKey(c) || counts[c] == 0) return false;
            counts[c]--;
        }

        return true;
    }
}