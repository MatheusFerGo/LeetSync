class Solution:
    def reverseList(self, no_cabeca_da_lista: Optional[ListNode]) -> Optional[ListNode]:
        no_anterior = None
        no_atual = no_cabeca_da_lista

        while no_atual is not None:
            proximo_no_temporario = no_atual.next

            no_atual.next = no_anterior

            no_anterior = no_atual

            no_atual = proximo_no_temporario

        return no_anterior