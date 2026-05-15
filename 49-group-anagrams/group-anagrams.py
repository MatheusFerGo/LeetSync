class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramas_agrupados_por_frequencia = defaultdict(list)

        for palavra_atual in strs:
            lista_de_frequencia_de_caracteres = [0] * 26
            
            for caractere_atual in palavra_atual:
                posicao_da_letra_no_alfabeto = ord(caractere_atual) - ord('a')
                lista_de_frequencia_de_caracteres[posicao_da_letra_no_alfabeto] += 1
        
            assinatura_de_frequencia_imutavel = tuple(lista_de_frequencia_de_caracteres)

            anagramas_agrupados_por_frequencia[assinatura_de_frequencia_imutavel].append(palavra_atual)

        return list(anagramas_agrupados_por_frequencia.values())