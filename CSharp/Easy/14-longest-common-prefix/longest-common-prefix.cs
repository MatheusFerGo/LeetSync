public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        if (strs == null || strs.Length == 0){
            return "";
        }

        Array.Sort(strs);
        string firstWord = strs[0];
        string lastWord = strs[strs.Length - 1];
        int i = 0;

        while (i < firstWord.Length && i < lastWord.Length && firstWord[i] == lastWord[i]){
            i ++;
        }

        return firstWord.Substring(0,i);
    }
}