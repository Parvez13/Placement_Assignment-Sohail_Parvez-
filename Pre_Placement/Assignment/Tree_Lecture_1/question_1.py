# Create a node
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Using DEPTH First Search
ans = float("-infinity")
def find_largest_subtree_sum(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data
    # left subtree
    left_subtree = find_largest_subtree_sum(root.left)
    # right subtree
    right_subtree = find_largest_subtree_sum(root.right)
    # Sum of all nodes
    sum_nodes = left_subtree + right_subtree + root.data
    # Temp max
    temp_max_trees = max(left_subtree, right_subtree)
    temp_max = max(temp_max_trees, sum_nodes)

    # global ans
    # ans = max(ans, temp_max)
    return sum_nodes

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(-2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(-6)
    root.right.right = TreeNode(2)
    print(find_largest_subtree_sum(root))
