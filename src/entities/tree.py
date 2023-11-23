from .node import Node

class BinaryTree:
    def __init__(self, data = None, node=None):
        if node:
            self.root = node
        elif data:
            self.root = Node(data)
        else:
            self.root = None
    
    #Percurso em pré ordem
    def pre_order_traversal(self, node='root'):
        if node == 'root':
            node = self.root

        if node is None:
            return None

        print(node)
        self.pre_order_traversal(node.left)
        self.pre_order_traversal(node.right)

    #Percurso em ordem
    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node)
        if node.right:
            self.inorder_traversal(node.right)
    
    
    def by_number_traversal(self, number: int, node=None, printed=False):
        '''
        Função responsável por percorrer os nós da árvore em ordem alfabética 
        e imprimir caso o tamanho seja o desejado pelo usuário
        '''
        if node is None:
            node = self.root

        if node.left:
            printed = self.by_number_traversal(number, node.left, printed)
        
        if len(node.data) == number:
            print(node)
            printed = True

        if node.right:
            printed = self.by_number_traversal(number, node.right, printed)

        return printed
        
    
    def by_alphabetic_traversal(self, init: str, end: str, node=None, printed=False):
        '''
        Função responsavel por percorrer os nos da arvore em ordem alfabetica 
        e printar caso a palavra esteja no intervalo desejado
        '''
        if node is None:
            node = self.root
        if node.left:
            printed = self.by_alphabetic_traversal(init, end, node.left, printed)
        if init <= node.data[0] and node.data[0] <= end:
            print(node)
            printed = True
        if node.right:
            printed = self.by_alphabetic_traversal(init, end, node.right, printed)
        
        return printed
    
    #Percurso em pós ordem
    def post_order_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.post_order_traversal(node.left)
        if node.right:
            self.post_order_traversal(node.right)
        print(f'palavra: {node.data} fesq: {node.left} fdir: {node.right}')

    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1    
        return hleft + 1

class BinarySearchTree(BinaryTree):
    def insert(self, node: Node):
        parent = None
        aux = self.root
        while aux:
            parent = aux
            if node.data < aux.data:
                aux = aux.left
            else:
                aux = aux.right
        if parent is None:
            self.root = node
        elif node.data < parent.data:
            parent.left = node
        else:
            parent.right = node

    def search(self, value):
        return self.__iterable_search(value, self.root)
    
    def remove(self, value, node=None):
        if node is None:
            node = self.root
        
        if node is None:
            return node
        
        if value < node.data:
            node.left = self.remove(value, node.left)
        elif value > node.data:
            node.right = self.remove(value, node.right)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            else:
                sub = self.__min(node.right)
                node.data = sub
                node.right = self.remove(sub, node.right)

        return node
    
    def __search(self, value, node):
        if node is None or node.data == value:
            return node
        if value < node.data:
            return self.__search(value, node.left)
        else:
            return self.__search(value, node.right)
        
    def __iterable_search(self, value, node):
        while node is not None and node.data != value:
            if value < node.data:
                node = node.left
            else:
                node = node.right

        return node is not None
    
    def __min(self, node=None):
        if node is None:
            node = self.root
        while node.left:
            node = node.left
        return node.data

    def __max(self, node=None):
        if node is None:
            node = self.root
        while node.right:
            node = node.right
        return node.data
