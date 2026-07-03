public class Solution {
    public ListNode MergeTwoLists(ListNode list1, ListNode list2) {
        ListNode no_falso_ancora = new ListNode(-1);
        ListNode ponteiro_atual = no_falso_ancora;

        while (list1 != null && list2 != null){
            if(list1.val <= list2.val){
                ponteiro_atual.next = list1;
                list1 = list1.next;
            }
            else{
                ponteiro_atual.next = list2;
                list2 = list2.next;
            }
            ponteiro_atual = ponteiro_atual.next;
        }

        if (list1 != null){
            ponteiro_atual.next = list1;
        }
        else{
            ponteiro_atual.next = list2;
        }

        return no_falso_ancora.next;
    }
}