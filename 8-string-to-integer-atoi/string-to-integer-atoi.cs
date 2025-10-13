public class Solution {
    public int MyAtoi(string s) {
        if(string.IsNullOrEmpty(s) || string.IsNullOrWhiteSpace(s)){
            return 0;
        }

        int i = 0;
        int sign = 1;
        long result = 0;
        int n = s.Length;

        while (i<n && s[i] == ' '){
            i++;
        }

        if (i<n && s[i] == '+' || s[i] == '-'){
            sign = (s[i] == '-') ? -1 : 1;
            i++;
        }

        while (i<n && Char.IsDigit(s[i])){
            int digit = s[i] - '0';
            result = result * 10 + digit;

            if (sign*result > int.MaxValue){
                return int.MaxValue;
            }

            if (sign*result < int.MinValue){
                return int.MinValue;
            }

            i++;
        }

        return (int)(sign*result);
    }
}