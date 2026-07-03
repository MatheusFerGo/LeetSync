class Solution:
    def middleNode(self, no_cabeca_da_lista: Optional[ListNode]) -> Optional[ListNode]:
        ponteiro_lento = no_cabeca_da_lista
        ponteiro_rapido = no_cabeca_da_lista

        while ponteiro_rapido is not None and ponteiro_rapido.next is not None:
            ponteiro_lento = ponteiro_lento.next
            ponteiro_rapido = ponteiro_rapido.next.next
        
        return ponteiro_lento
