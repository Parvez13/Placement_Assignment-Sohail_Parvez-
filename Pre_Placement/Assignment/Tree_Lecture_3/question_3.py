class Node:
    def __init__(self, data):
        self.data = data 
        self.right = None 
        self.left = None 
        
class Stack:  # just for reference
    def __init__(self):
        self.a = []

    def push(self, b):
        self.a.append(b)

    def peek(self):
        return self.a[-1]

    def pop(self):
        return self.a.pop()

    def isEmpty(self):
        return len(self.a) == 0

    def show(self):
        return self.a

def paths(troot): 
    current = troot
    s = Stack()
    s.push(current)
    s.push(current.data)
    s.push(current.data)

    while not s.isEmpty():
        pathsum = s.pop()
        path = s.pop()
        current = s.pop()

        if not current.left and not current.right:
            print('path: %s, pathsum: %d' % (path, pathsum))

        if current.right:
            rightstr = path + "->" + str(current.right.key)
            rightpathsum = pathsum * 10 + current.right.key
            s.push(current.right)
            s.push(rightstr)
            s.push(rightpathsum)

        if current.left:
            leftstr = path + "->" + str(current.left.key)
            leftpathsum = pathsum * 10 + current.left.key
            s.push(current.left)
            s.push(leftstr)
            s.push(leftpathsum)

if __name__ == '__main__':
    root = Node(6)
    root.left = Node(3)
    root.right = Node(5)
    root.left.right = Node(5)
    root.left.left = Node(2)
    root.left.right.left = Node(7)
    root.left.right.right = Node(4)
    root.right.left = Node(4)
    print(paths(root))