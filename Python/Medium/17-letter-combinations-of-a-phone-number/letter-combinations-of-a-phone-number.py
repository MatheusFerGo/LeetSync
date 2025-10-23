class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return [] 

        dicionario = {'2': "abc",'3': "def",'4': "ghi",'5': "jkl",'6': "mno",'7': "pqrs",'8': "tuv",'9': "wxyz"}

        resultados = [""]

        for digito in digits:
            letras_do_digito = dicionario[digito]
            novos_resultados = []

            for prefixo in resultados:
                for letra in letras_do_digito:
                   novos_resultados.append(prefixo + letra)

            resultados = novos_resultados

        return resultados