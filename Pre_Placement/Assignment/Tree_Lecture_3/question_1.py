# Convert binary tree to double linked list inorder traversal
# Create a node 
class Node:
    def __init__(self, data):
        self.data = data 
        self.right = None 
        self.left = None 

def BT_DLL(root):
    if root is None:
        return root 
    # Convert left subtree and link to root 
    if root.left:
        # left 
        left = BT_DLL(root.left)
        #Find inorder predecessor, after this loop 
        while left.right:
            left = left.right 
        
        # Make root as next of predecessor
        left.right = root 
        root.left = left 
        
    # Convert right subtree
    if root.right:
        right = BT_DLL(root.right)
        while right.left:
            right = right.left 
        right.left = root 
        root.right = right 
    return root 

def BTToDLL(root):
    if root is None:
        return root 
    root = BT_DLL(root)

    # We need pointer to left most
    # node which is head of the
    # constructed Doubly Linked list
    while root.left:
        root = root.left

    return root


def print_list(head):
    """Function to print the given
       doubly linked list"""
    if head is None:
        return
    while head:
        print(head.data, end=" ")
        head = head.right

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)
    
    head = BTToDLL(root)
    print_list(head)