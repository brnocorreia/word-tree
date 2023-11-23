class Node:
    def __init__(self, data: str):
        self.data = data
        self.right = None
        self.left = None
        self.next = None
    
    def __str__(self):
        return str(self.data)
