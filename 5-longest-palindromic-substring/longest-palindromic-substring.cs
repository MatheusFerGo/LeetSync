public class Solution {
    public string LongestPalindrome(string s) {
        if(string.IsNullOrEmpty(s)){
            return "";
        }

        int start = 0;
        int end = 0;

        // O loop principal. Ele vai passar por cada indice 'i' da string.
        // Cada 'i' será o "ponto de partida" para procurarmos um palindromo.
        for (int i = 0; i < s.Length; i++){
            
            // CASO 1: Palindromo de comprimento IMPAR.
            // O centro é o único carctere. Ex: "r a c e c a r" (o centro é 'e').
            // Chamamos a função passando 'i' e 'i + 1' como o centro. 
            int len1 = ExpandAroundCenter(s, i, i);

            // CASO 2: Palindromo de comprimento PAR.
            // O centro está entre dosi caracteres. Ex: "a b | b a"
            int len2 = ExpandAroundCenter(s, i, i + 1);
            
            // Nós queremos o maior palindromo, não importa se é par ou impar.
            // Então, pegamos o maior comprimento entre os dois casos.
            int len = Math.Max(len1, len2);



            if(len > end - start){
                start = i - (len-1) / 2;
                end = i + len / 2;
            }
        }

        int length = end - start + 1;
        return s.Substring(start, length);
    }

    private int ExpandAroundCenter(string s, int left, int right){
        while (left >= 0 && right < s.Length && s[left] == s[right]){
            left--;
            right++;
        }

        return right - left - 1;
    }
}