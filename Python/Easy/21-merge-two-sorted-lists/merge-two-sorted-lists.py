class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        no_falso_ancora = ListNode(val=-1)
        ponteiro_atual = no_falso_ancora

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                ponteiro_atual.next = list1
                list1 = list1.next
            else:
                ponteiro_atual.next = list2
                list2 = list2.next
            
            ponteiro_atual = ponteiro_atual.next

        if list1 is not None:
            ponteiro_atual.next = list1
        else:
            ponteiro_atual.next = list2
        
        return no_falso_ancora.next