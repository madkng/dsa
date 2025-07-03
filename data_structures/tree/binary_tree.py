"""
Binary Tree is a non-linear hierarchical data structure that consists of nodes,
where each node has at most two children referred to as the left child and the right child.

The topmost node is called the root, and each node can have its own subtrees.
The bottommost nodes are called leaves, which do not have any children.

A binary tree can be used to represent hierarchical data,
such as file systems, organizational structures, and more.

Terminologies:
- Node: A single element in the tree containing data and references to its children.
- Root: The topmost node in the tree.
- Parent: A node that has one or more children.
- Child: A node that is a descendant of another node.
- Leaf: A node that does not have any children.
- Internal Node: A node that has at least one child.
- Subtree: A tree formed by a node and its descendants.
- Depth: The length of the path from the root to a node.
- Height: The length of the longest path from a node to a leaf.


Operations on Binary Trees:
- Traversal: Visiting all nodes in a specific order.
    Tree traversal algorithms can be classified into two categories:
    1. Depth-First Traversal (DFT):
        - Pre-order Traversal: Visit the root, then left subtree, then right subtree.
        - In-order Traversal: Visit the left subtree, then root, then right subtree.
        - Post-order Traversal: Visit the left subtree, then right subtree, then root.

    2. Breadth-First Traversal (BFT):
        - Level-order Traversal: Visit nodes level by level, starting from the root.

- Insertion in a Binary Tree: Adding a new node to the tree.
    Since in a binary tree, there are no specific rules for insertion,
    a new node can be added at the first available position in the tree.

    1.- Create a new node in the case of an empty tree.
    2.- If the tree is not empty, traverse the tree to find the first available
    position (usually the leftmost position at the last level using Level-Order Traversal).

- Searching in a Binary Tree: Finding a node with a specific value.
    This can be done using Depth-First Search (DFS) or Breadth-First Search (BFS) algorithms.

    - Depth-First Search (DFS): Traverse the tree by going deep into each branch
      before backtracking.

    - Breadth-First Search (BFS): Traverse the tree level by level,
      visiting all nodes at the current level before moving to the next level.

- Deletion in a Binary Tree: Removing a node from the tree.
    Deletion in a binary tree is not as straightforward as insertion.
    The process typically involves finding the node to be deleted,
    replacing it with a suitable node (usually the rightmost node in the left subtree or
    the leftmost node in the right subtree), and then removing the original node.

Complexity Analysis:
- Time Complexity:
    - In-order, Pre-order, and Post-order Traversal: O(n), where n is the number of nodes.
    - Level-order Traversal: O(n), where n is the number of nodes.
    - Insertion: O(n) in the worst case, O(1) if the tree is empty.
    - Searching: O(n) in the worst case, O(1) if the root is the target.
    - Deletion: O(n) in the worst case, O(1) if the node to be deleted is the root.

- Space Complexity:
    - In-order, Pre-order, and Post-order Traversal: O(h), where h is the height of the tree.
    - Level-order Traversal: O(n) for the queue used in BFS.
    - Insertion: O(n) for the queue used in BFS.
    - Searching: O(h) for the recursive stack in DFS or O(n) for the queue in BFS.
    - Deletion: O(n) for the queue used in BFS.
"""
from collections import deque
from typing import Any
class Node:
    """
    A Node class represents a single node in a binary tree.
    """
    def __init__(self, data:Any):
        self.data = data
        self.left = None
        self.right = None

def in_order_dfs(node:Node) -> None:
    """
    In-order Depth-First Search (DFS) traversal of a binary tree.

    This function visits the left subtree,
    then the current node, and finally the right subtree.

    It performs an operation with the node data at each visit.
    :param node: The current node in the binary tree.
    :return: None
    """
    if node is None:
        return

    in_order_dfs(node.left)
    print(f"Perform operation with node data: {node.data}")
    in_order_dfs(node.right)

def pre_order_dfs(node:Node) -> None:
    """
    Pre-order Depth-First Search (DFS) traversal of a binary tree.

    This function visits the current node first,
    then the left subtree, and finally the right subtree

    :param node: The current node in the binary tree.
    :return: None
    """
    if node is None:
        return

    print(f"Perform operation with node data: {node.data}")
    pre_order_dfs(node.left)
    pre_order_dfs(node.right)

def post_order_dfs(node:Node) -> None:
    """
    Post-order Depth-First Search (DFS) traversal of a binary tree.

    This function visits the left subtree first,
    then the right subtree, and finally the current node.

    :param node: The current node in the binary tree.
    :return: None
    """
    if node is None:
        return

    post_order_dfs(node.left)
    post_order_dfs(node.right)
    print(f"Perform operation with node data: {node.data}")

def level_order_bfs(root:Node) -> None:
    """
    Level-order Breadth-First Search (BFS) traversal of a binary tree.

    This function visits nodes level by level, starting from the root.
    It uses a queue to keep track of nodes at each level.

    :param root: The root node of the binary tree.
    :return: None
    """
    if root is None:
        return 
    
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(f"Perform operation with node data: {node.data}")
        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

def insert_node(root:Node, data:Any) -> Node:
    """
    Inserts a new node with the given data into the binary tree.
    The new node is added at the first available position.

    :param root: The root node of the binary tree.
    :param data: The data for the new node.
    :return: The root node of the binary tree after insertion.
    """
    if root is None:
        return Node(data)

    queue = [root]
    while queue:
        current = queue.pop(0)

        # If the left child is None, insert the new node here
        if current.left is None:
            current.left = Node(data=data)
            break

        # If the left child is not None, add it to the queue for further processing
        else:
            queue.append(current.left)

        # If the left child is not None, check the right child
        if current.right is None:
            current.right = Node(data=data)
            break

        # If the right child is not None, add it to the queue for further processing
        else:
            queue.append(current.right)

    # Return the root node after insertion
    return root

def delete_node(root:Node, target:Any) -> Node:
    if not root:
        return None

    # Use a queue to perform BFS
    queue = deque([root])
    target_node = None

    # Find the target node using BFS
    while queue:
        current = queue.popleft()

        if current.data == target:
            target_node = current
            break

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    if target_node is None:
        return root

    # Find the deepest rightmost node and its parent
    last_node = None
    last_parent = None
    queue = deque([(root, None)])

    while queue:
        current, parent = queue.popleft()

        last_node = current
        last_parent = parent

        if current.left:
            queue.append((current.left, current))

        if current.right:
            queue.append((current.right, current))

    target_node.data = last_node.data

    # Remove the last node from the tree
    if last_parent:
        if last_parent.left == last_node:
            last_parent.left = None
        else:
            last_parent.right = None

    else:
        # If the tree has only one node, set root to None
        return None

    return root

def search_dfs(node:Node, target:Any) -> bool:
    """
    Searches for a node with the specified target value using Depth-First Search (DFS).

    :param node: The current node in the binary tree.
    :param target: The value to search for.
    :return: True if the target is found, False otherwise.
    """
    if node is None:
        return False

    if node.data == target:
        return True

    # Search in left and right subtrees
    return search_dfs(node.left, target) or search_dfs(node.right, target)

def search_bfs(root:Node, target:Any) -> bool:
    """
    Searches for a node with the specified target value using Breadth-First Search (BFS).

    :param root: The root node of the binary tree.
    :param target: The value to search for.
    :return: True if the target is found, False otherwise.
    """
    if root is None:
        return False

    queue = [root]
    while queue:
        node = queue.pop(0)

        if node.data == target:
            return True

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return False

if __name__ == "__main__":
    first_node = Node(data=2)
    second_node = Node(data=3)
    third_node = Node(data=4)
    fourth_node = Node(data=5)


    first_node.left = second_node
    first_node.right = third_node
    second_node.left = fourth_node

    print("In-order DFS Traversal:")
    in_order_dfs(first_node) # Output: 5,3,2,4
    print("\nPre-order DFS Traversal:")
    pre_order_dfs(first_node) # Output: 2,3,5,4
    print("\nPost-order DFS Traversal:")
    post_order_dfs(first_node) # Output: 5,3,4,2
    print("\nLevel-order BFS Traversal:")
    level_order_bfs(first_node) # Output: 2,3,4,5

    fifth_node = Node(data=6)
    root_node = insert_node(first_node, fifth_node.data)
    print("\nAfter inserting a new node with data 6:")
    print("In-order DFS Traversal after insertion:")
    in_order_dfs(root_node)  # Output: 5,3,6,2,4

    print("\nSearching for node with data 4 using DFS:")
    found_dfs = search_dfs(root_node, 4)
    print(f"Node with data 4 found: {found_dfs}")  # Output: True
    print("\nSearching for node with data 7 using DFS:")
    found_dfs = search_dfs(root_node, 7)
    print(f"Node with data 7 found: {found_dfs}")  # Output: False

    print("\nSearching for node with data 4 using BFS:")
    FOUND_BFS = search_bfs(root_node, 4)
    print(f"Node with data 4 found: {FOUND_BFS}")  # Output: True
    print("\nSearching for node with data 7 using BFS:")
    FOUND_BFS = search_bfs(root_node, 7)
    print(f"Node with data 7 found: {FOUND_BFS}")  # Output: False

    print("\nDeleting node with data 3:")
    root_node = delete_node(root_node, 3)
    print("In-order DFS Traversal after deletion:")
    in_order_dfs(root_node)  # Output: 5, 6, 2, 4
