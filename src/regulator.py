from src.entities.linked_list import LinkedList
from src.entities.node import Node
from .entities.tree import BinarySearchTree

class Regulator:
    def __init__(self) -> None:
        self.tree = BinarySearchTree()
        self.list_1 = LinkedList()
        self.list_2 = LinkedList()

    def insert_use_case(self, value: str):
        res = self.tree.search(value)
        if not res:
            node = Node(value)
            self.tree.insert(node)
            if len(value) < 6:
                self.list_1.insert(node)
            else: 
                self.list_2.insert(node)
            print('palavra inserida:', value)
        else:
            print('palavra ja existente:', value)

    def remove_use_case(self, value: str):
        if not self.tree.search(value):
            print('palavra inexistente:', value)
        else:
            self.tree.remove(value)
            if len(value) < 6:
                self.list_1.remove(value)
            else:
                self.list_2.remove(value) 
    
    def search_use_case(self, value: str):
        res = self.tree.search(value)
        if not res:
            print('palavra inexistente:', value)
        else:
            print('palavra ja existente:', value)

    def list_use_case(self, value: int):
        match value:
            case 1:
                self.list_1.display_all()
            case 2:
                self.list_2.display_all()
    
    def number_traversal_use_case(self, number: int):
        if not self.tree.by_number_traversal(number):
            print('lista vazia')
        
    def alphabetic_traversal_use_case(self, init: str, end: str):
        if not self.tree.by_alphabetic_traversal(init, end):
            print('lista vazia')
    
    def post_order(self):
        self.tree.post_order_traversal()