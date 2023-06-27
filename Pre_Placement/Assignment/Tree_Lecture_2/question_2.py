# Find the distance between two nodes 
class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right= None 
    
# Find the least Common ancestor
def find_least_common_ancestor(root, n1, n2):
    # Base case 
    if root is None or root==n1 or root==n2:
        return root 
    left = find_least_common_ancestor(root.left, n1, n2)
    right = find_least_common_ancestor(root.right, n1, n2)
    if left is None:
        return right 
    if right is None:
        return left 
    else:
        return root 

# Find the distance from ancestor to node 
def find_distance_from_ancestor_node(root, data):
    if root is None:
        return -1
    # Node is found then 
    if root.data == data:
        return 0 
    left = find_distance_from_ancestor_node(root.left, data)
    right = find_distance_from_ancestor_node(root.right, data)
    distance = max(left, right)
    return distance + 1 if distance >=0 else -1 

# Find the distance between two nodes 
def find_distance_between_two_nodes(root, n1, n2):
    lca = find_least_common_ancestor(root, n1,n2)
    return find_distance_from_ancestor_node(lca, n1) + find_distance_from_ancestor_node(lca, n2) if lca else -1
    
if __name__ == '__main__':
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)
    root.right.right = Node(14)
    print(f"Distance between {6} and {14} is {find_distance_between_two_nodes(root, n1=6, n2=14)}")
  