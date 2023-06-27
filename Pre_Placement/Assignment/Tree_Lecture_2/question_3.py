# Convert binary tree to doubly linked list
class Node:
    def __init__(self, data):
        self.data = data 
        self.right = None 
        self.left = None 

prev= None 
def BinaryTree2DLL(root):
    # Base case 
    if root is None:
        return root 
    # Recursively convert left subtree 
    head = BinaryTree2DLL(root.left)
    global prev 
    if prev is None:
        head = root 
    else:
        root.left= prev
        prev.right = root 
        
    # update prev 
    prev = root
    # Recursively convert right subtree 
    BinaryTree2DLL(root.right)
    return head
