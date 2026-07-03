public class Solution {
    public ListNode MiddleNode(ListNode no_cabeca_da_lista) {
        ListNode ponteiro_lento = no_cabeca_da_lista;
        ListNode ponteiro_rapido = no_cabeca_da_lista;

        while (ponteiro_rapido != null && ponteiro_rapido.next != null){
            ponteiro_lento = ponteiro_lento.next;
            ponteiro_rapido = ponteiro_rapido.next.next;
        }
        
        return ponteiro_lento;
    }
}