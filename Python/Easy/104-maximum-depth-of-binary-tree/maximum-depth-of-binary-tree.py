# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, no_raiz_da_arvore: Optional[TreeNode]) -> int:
        if no_raiz_da_arvore is None:
            return 0

        profundidade_do_lado_esquerdo = self.maxDepth(no_raiz_da_arvore.left)

        profundidade_do_lado_direito = self.maxDepth(no_raiz_da_arvore.right)

        maior_profundidade_entre_os_lados = (max(profundidade_do_lado_esquerdo, profundidade_do_lado_direito))

        return 1 + maior_profundidade_entre_os_lados