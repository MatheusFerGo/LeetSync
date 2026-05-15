public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        var anagramMap = new Dictionary<string, List<string>>();

        foreach (string word in strs) {
            char[] charArray = word.ToCharArray();
            Array.Sort(charArray);
            string sortedWord = new string(charArray);

            if (!anagramMap.ContainsKey(sortedWord)){
                anagramMap[sortedWord] = new List<string>();
            }
            anagramMap[sortedWord].Add(word);
        }

        return anagramMap.Values.Cast<IList<string>>().ToList();
    }
}