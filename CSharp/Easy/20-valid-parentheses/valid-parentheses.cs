public class Solution {
    public bool IsValid(string s) {
        Stack<char> bracketStack = new Stack<char>();

        Dictionary<char, char> bracketMap = new Dictionary<char, char>{
            { ')', '(' },
            { '}', '{' },
            { ']', '[' }
        };

        foreach (char currentChar in s){
            if (bracketMap.ContainsKey(currentChar)){
                if (bracketStack.Count == 0 || bracketStack.Pop() != bracketMap[currentChar]){
                    return false;
                }
            }
            else{
                bracketStack.Push(currentChar);
            }
        }
        return bracketStack.Count == 0;
    }
}