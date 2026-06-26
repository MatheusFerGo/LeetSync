public class Solution {
    public ListNode ReverseList(ListNode no_cabeca_da_lista) {
        ListNode no_anterior = null;
        ListNode no_atual = no_cabeca_da_lista;

        while (no_atual != null) {
            ListNode proximo_no_temporario = no_atual.next;

            no_atual.next = no_anterior;

            no_anterior = no_atual;

            no_atual = proximo_no_temporario;
        }

        return no_anterior;
    }
}