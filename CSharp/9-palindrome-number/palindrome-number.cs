public class Solution {
    public bool IsPalindrome(int x) {
        string originalString = x.ToString();
        char[] charArray = originalString.ToCharArray();

        Array.Reverse(charArray);

        string reversedString = new string(charArray);

        return originalString.Equals(reversedString);
    }
}