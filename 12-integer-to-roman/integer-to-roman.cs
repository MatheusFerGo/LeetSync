public class Solution {
    public string IntToRoman(int num) {
        string[] ones = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
        string[] tens = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        string[] hundreds = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        string[] thousands = {"", "M", "MM", "MMM"};

        StringBuilder roman = new StringBuilder();

        roman.Append(thousands[num / 1000]);
        roman.Append(hundreds[(num % 1000) / 100]);
        roman.Append(tens[(num % 100) / 10]);
        roman.Append(ones[num % 10]);

        return roman.ToString();
    }
}