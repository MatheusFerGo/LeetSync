class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        total_de_linhas = len(triangle)

        if total_de_linhas == 1:
            return triangle[0][0]

        linha_atual = total_de_linhas - 2

        while linha_atual >= 0:
            for coluna_atual in range(len(triangle[linha_atual])):
                filho_esquerdo = triangle[linha_atual + 1][coluna_atual]
                filho_direito = triangle[linha_atual + 1][coluna_atual + 1]
            
                menor_caminho_abaixo = min(filho_esquerdo, filho_direito)

                triangle[linha_atual][coluna_atual] += menor_caminho_abaixo

            linha_atual -= 1
            
        return triangle[0][0]