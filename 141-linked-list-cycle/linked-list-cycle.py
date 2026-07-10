class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        ponteiro_rapido = head 
        ponteiro_lento = head

        while ponteiro_rapido is not None and ponteiro_rapido.next is not None:
            ponteiro_lento = ponteiro_lento.next
            ponteiro_rapido = ponteiro_rapido.next.next

            if ponteiro_rapido == ponteiro_lento:
                return True

        return False