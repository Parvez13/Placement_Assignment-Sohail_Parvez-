class node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


preIndex = 0


def search(arr, strt, end, value):

    for i in range(strt, end + 1):
        if (arr[i] == value):
            return i


def buildTree(inn, pre, inStrt, inEnd):

    global preIndex

    if (inStrt > inEnd):
        return None

    tNode = node(pre[preIndex])
    preIndex += 1

    # If this node has no children
    # then return
    if (inStrt == inEnd):
        return tNode

    # Else find the index of this
    # node in Inorder traversal
    inIndex = search(inn, inStrt,
                     inEnd, tNode.data)

    tNode.left = buildTree(inn, pre, inStrt,
                           inIndex - 1)
    tNode.right = buildTree(inn, pre,
                            inIndex + 1, inEnd)

    return tNode

# function to compare Postorder traversal
# on constructed tree and given Postorder


def checkPostorder(node, postOrder, index):
    if (node == None):
        return index

    # first recur on left child
    index = checkPostorder(node.left,
                           postOrder,
                           index)

    # now recur on right child
    index = checkPostorder(node.right,
                           postOrder,
                           index)

    if (node.data == postOrder[index]):
        index += 1
    else:
        return - 1

    return index
