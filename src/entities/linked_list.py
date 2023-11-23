from .node import Node

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert(self, node: Node):
        
        if self.head is None or node.data < self.head.data:
            node.next = self.head
            self.head = node
            return

        current = self.head

        while current.next is not None and current.next.data < node.data:
            current = current.next

        node.next = current.next
        current.next = node
    
    def remove(self, word: str):
        pant = None
        p = self.head
        while (p != None) and (p.data != word):
            pant = p
            p = p.next
        if (p == None):
            return False
        if (pant == None):
            self.head = p.next
        else:
            pant.next = p.next
        return True
    
    def display_all(self):
        if not self.head:
            return print('lista vazia')
        p = self.head
        while p:
            print(p.data)
            p = p.next

    def display_by_number(self, number: int):
        hasMatch = False
        p = self.head
        while p:
            if len(p.data) == number:
                hasMatch = True
                print(p.data)
            p = p.next
        if not hasMatch:
            print('lista vazia')

    def display_by_alphabetic(self, init: str, end: str):
        '''
            Função responsável por imprimir todos os nós da lista num intervalo do alfabeto (ex.: Palavras de A até D)
        '''
        hasMatch = False
        p = self.head
        while p:
            if init <= p.data[0] and p.data[0] <= end:
                hasMatch = True
                print(p.data)
            p = p.next
        if not hasMatch:
            print('lista vazia')