public class Solution {
    public bool IsValid(string s) {

        var stack = new Stack<char>();

        var bracketPairs = new Dictionary<char, char>
        {
            { ')', '(' },
            { '}', '{' },
            { ']', '[' }
        };

        foreach (char c in s) 
        {
            if (bracketPairs.ContainsKey(c)) 
            {
                if (stack.Count == 0 || stack.Pop() != bracketPairs[c]) 
                {
                    return false;
                }
            }
            else 
            {
                stack.Push(c);
            }
        }

        return stack.Count == 0;
    }
}