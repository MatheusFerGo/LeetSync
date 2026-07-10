public class Solution {
    public bool HasCycle(ListNode head) {
        if(head == null || head.next == null){
            return false;
        }

        ListNode ponteiro_lento = head;
        ListNode ponteiro_rapido = head;

        while(ponteiro_rapido != null && ponteiro_rapido.next != null){
            ponteiro_lento = ponteiro_lento.next;
            ponteiro_rapido = ponteiro_rapido.next.next;

            if(ponteiro_lento == ponteiro_rapido){
                return true;
            }
        }
        return false;
    }
}