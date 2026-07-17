public class Solution {
    public ListNode RemoveNthFromEnd(ListNode head, int n) {
        ListNode no_falso_ancora = new ListNode(0, head);

        ListNode ponteiro_tras = no_falso_ancora;
        ListNode ponteiro_frente = no_falso_ancora;

        for(int i = 0; i < n; i++){
            ponteiro_frente = ponteiro_frente.next;
        }

        while(ponteiro_frente.next != null){
            ponteiro_frente = ponteiro_frente.next;
            ponteiro_tras = ponteiro_tras.next;
        }

        ponteiro_tras.next = ponteiro_tras.next.next;

        return no_falso_ancora.next;
    }
}