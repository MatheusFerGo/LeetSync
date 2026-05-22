/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public int MaxDepth(TreeNode no_raiz_da_arvore) {
        if(no_raiz_da_arvore == null){
            return 0;
        }

        int profundidade_do_lado_esquerdo = MaxDepth(no_raiz_da_arvore.left);

        int profundidade_do_lado_direito = MaxDepth(no_raiz_da_arvore.right);

        int maior_profundidade_entre_lados = Math.Max(profundidade_do_lado_direito,profundidade_do_lado_esquerdo);

        return 1 + maior_profundidade_entre_lados;
    }
}