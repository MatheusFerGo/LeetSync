public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> dicionario_de_anagramas_agrupados = new Dictionary<string, List<string>>();

        foreach (string palavra_atual in strs){
            int[] contagem_de_frequencia_de_letras = new int[26];
            
            foreach (char caractere_atual in palavra_atual){
                int indice_da_letra_no_alfabeto = caractere_atual - 'a';
                contagem_de_frequencia_de_letras[indice_da_letra_no_alfabeto]++;
            }

            StringBuilder construtor_de_chave_identificadora = new StringBuilder();
            foreach (int quantidade_da_letra in contagem_de_frequencia_de_letras){
                construtor_de_chave_identificadora.Append('#');
                construtor_de_chave_identificadora.Append(quantidade_da_letra);
            }
            string chave_identificadora_de_anagrama = construtor_de_chave_identificadora.ToString();

            if (!dicionario_de_anagramas_agrupados.ContainsKey(chave_identificadora_de_anagrama)){
                dicionario_de_anagramas_agrupados[chave_identificadora_de_anagrama] = new List<string>();
            }

            dicionario_de_anagramas_agrupados[chave_identificadora_de_anagrama].Add(palavra_atual);            
        }
        return new List<IList<string>>(dicionario_de_anagramas_agrupados.Values);
    }
}