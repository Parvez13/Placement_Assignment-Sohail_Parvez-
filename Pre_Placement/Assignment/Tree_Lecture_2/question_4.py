class newnode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = self.nextRight = None

def connect(root):

    # Base condition
    if root is None:
        return

    # Create an empty queue like level order traversal
    queue = []
    queue.append(root)
    while len(queue) != 0:

        # size indicates no. of nodes at current level
        size = len(queue)

        # for keeping track of previous node
        prev = newnode(None)
        for i in range(size):
            temp = queue.pop(0)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
            if prev != None:
                prev.nextRight = temp
                prev = temp
        prev.nextRight = None
