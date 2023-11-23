from src.entities.tree import BinarySearchTree

bst = BinarySearchTree()

bst.insert('lua')
bst.insert('guitarra')
bst.insert('moradia')
bst.insert('agua')
bst.insert('mar')
bst.insert('novelo')
bst.insert('ouro')

# bst.pre_order_traversal()
# print('\n-----')
# bst.post_order_traversal()
# print('\n-----')
# bst.inorder_traversal()
res = bst.search('maraa')
print(res)