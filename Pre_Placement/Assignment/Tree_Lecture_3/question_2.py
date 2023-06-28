# A binary tree node
class Node:

    # Constructor to create
    # a new node
    def __init__(self, data):

        self.data = data
        self.right = None
        self.left = None


def flipBinaryTree(root):

    # Base Cases
    if root is None:
        return root

    if (root.left is None and
            root.right is None):
        return root

    # Recursively call the
    # same method
    flippedRoot = flipBinaryTree(root.left)

    # Rearranging main root Node
    # after returning from
    # recursive call
    root.left.left = root.right
    root.left.right = root
    root.left = root.right = None

    return flippedRoot

