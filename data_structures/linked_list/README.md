# Linked List Data Structure

A **Linked List** is a linear data structure where elements are stored in nodes, and each node points to the next node in the sequence. Unlike arrays, linked list elements are not stored at contiguous memory locations.

## 🧱 Basic Structure

Each node in a linked list contains:

- **Data**: The value or information stored
- **Next**: A reference (pointer) to the next node

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

## 🔄 Types of Linked Lists

1. **Singly Linked List**
   Each node points only to the next node
2. **Doubly Linked List**
   Each node points to both next and previous nodes
3. **Circular Linked List**
   The last node points back to the first node

🔑 ## Key Characteristics

- **Dynamic size**: Grows and shrinks as needed
- **Memory efficiency**: Allocates memory as needed at runtime
- **Insertion/Deletion**: More efficient than arrays (O(1) for head operations)
- **Random access**: Not possible (access is sequential)

## ⚙️ Common Operations

| Operation | Time Complexity |
| --------- | --------------- |
| Access    | O(n)            |
| Search    | O(n)            |
| Insertion | O(1) at head    |
|           | O(n) elsewhere  |
| Deletion  | O(1) at head    |
|           | O(n) elsewhere  |

## ✔️ Advantages

- No need to pre-allocate memory
- Efficient insertion/deletion compared to arrays
- Can grow to any size (within memory limits)

## ❌ Disadvantages

- Uses more memory than arrays (for pointers)
- No constant-time access to elements
- Cache performance is worse than arrays

## 💡 Example Usage

Linked lists are commonly used for:

- Implementing stacks and queues
- Memory management systems
- Polynomial representation
- Hash table collision handling
- Many other advanced data structures

## 🎨 Visualization

**Singly Linked List**

```none
[Data|Next] -> [Data|Next] -> [Data|Next] -> None
```

**Doubly Linked List**

```none
[Prev|Data|Next] <-> [Prev|Data|Next] <-> [Prev|Data|Next]
```

## 🚀 Implementation

Basic operations include:

- Node creation
- List traversal
- Insertion (head/middle/tail)
- Deletion (head/middle/tail)
- Search operations

```python
# Example: Creating a simple linked list
head = Node(10)
second = Node(20)
third = Node(30)

head.next = second
second.next = third
```
