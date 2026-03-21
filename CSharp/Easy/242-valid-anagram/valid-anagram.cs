public class Solution {
    public bool IsAnagram(string s, string t) {
        return s.OrderBy(c => c).SequenceEqual(t.OrderBy(c => c));
    }
}