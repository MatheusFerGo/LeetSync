class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        no_falso_ancora = ListNode(0, head)

        ponteiro_tras = no_falso_ancora
        ponteiro_frente = no_falso_ancora

        for _ in range (n):
            ponteiro_frente = ponteiro_frente.next

        while ponteiro_frente.next is not None:
            ponteiro_frente = ponteiro_frente.next
            ponteiro_tras = ponteiro_tras.next

        ponteiro_tras.next = ponteiro_tras.next.next

        return no_falso_ancora.next