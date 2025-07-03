# Tree Data Structure

A **Tree** is a hierarchical data structure consisting of nodes, with a single node designated as the root. Each node may have zero or more child nodes, and there are no cycles. Trees are widely used in computer science for representing hierarchical relationships, organizing data, and enabling efficient searching and sorting.

## 🧱 Basic Structure

Each node in a tree contains:

- **Data**: The value or information stored
- **Children**: References (pointers) to child nodes
- **Parent**: (except for the root) Reference to the parent node

A **Binary Tree** is a special type of tree where each node has at most two children, commonly referred to as the left and right child.

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

## 🔄 Types of Trees

1. **Binary Tree**: Each node has at most two children.
2. **Binary Search Tree (BST)**: A binary tree where the left child is less than the parent and the right child is greater or equal.
3. **AVL Tree**: A self-balancing binary search tree.
4. **Red-Black Tree**: A balanced binary search tree with color properties.
5. **Trie (Prefix Tree)**: Used for efficient retrieval of strings.
6. **Heap**: A complete binary tree used for priority queues.
7. **N-ary Tree**: Each node can have up to N children.

## 🔑 Key Characteristics

- **Hierarchical structure**: Parent-child relationships
- **No cycles**: Unique path between any two nodes
- **Recursive definition**: Each subtree is itself a tree
- **Depth/Height**: Number of edges from root to leaf

## ⚙️ Common Operations

| Operation      | Description                                 | Time Complexity (BST) |
| -------------- | ------------------------------------------- | --------------------- |
| Access/Search  | Find a node with a given value              | O(log n) avg, O(n) worst |
| Insertion      | Add a new node                              | O(log n) avg, O(n) worst |
| Deletion       | Remove a node                               | O(log n) avg, O(n) worst |
| Traversal      | Visit all nodes (inorder, preorder, postorder, level order) | O(n) |

## ✔️ Advantages

- Efficient searching, insertion, and deletion (in balanced trees)
- Hierarchical data representation (e.g., file systems, organization charts)
- Foundation for advanced data structures (heaps, tries, segment trees)

## ❌ Disadvantages

- More memory usage due to pointers
- Can become unbalanced, leading to degraded performance (O(n) in worst-case BST)

## 💡 Example Use Cases

- Expression parsing and evaluation (expression trees)
- Database indexing (B-trees, AVL trees)
- File system directories
- Autocomplete and spell-check (tries)
- Priority queues (heaps)
- Network routing (spanning trees)

## 🎨 Visualization

**Binary Tree**

```none
        [10]
       /    \
     [5]   [15]
       \
       [8]
```

**General Tree**

```none
        [A]
      /  |  \
    [B] [C] [D]
         |
        [E]
```

## 🚀 Implementation Example

```python
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            return self.left.contains(value) if self.left else False
        else:
            return self.right.contains(value) if self.right else False

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value)
        if self.right:
            self.right.inorder()
```

## 🌐 Language Implementations

### Python

- Use classes to define nodes and tree structure.
- Standard library: `collections` for tree-like structures (not a built-in tree).

### Java

- Use classes for nodes and tree logic.
- Standard library: `TreeMap`, `TreeSet` (Red-Black Trees).

---

**Key Insight:**  
Trees are essential for representing hierarchical data and enabling efficient searching, sorting, and organization. Mastering tree structures is crucial for advanced algorithms and system