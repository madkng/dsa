# Stacks and Queues Data Structures

Stacks and Queues are fundamental data structures used in computer science for managing collections of elements. They are widely used in algorithms, system design, and problem-solving.

## 🧱 Basic Structure

### Stack

A **Stack** is a linear data structure that follows the **Last In, First Out (LIFO)** principle. The last element added to the stack is the first one to be removed.

```python
# Example of a stack using a list
stack = []
stack.append(1)  # Push
stack.append(2)
stack.pop()      # Pop
```

### Queue

A **Queue** is a linear data structure that follows the **First In, First Out (FIFO)** principle. The first element added to the queue is the first one to be removed.

```python
# Example of a queue using collections.deque
from collections import deque
queue = deque()
queue.append(1)  # Enqueue
queue.append(2)
queue.popleft()  # Dequeue
```

## 🔄 Types of Stacks and Queues

1. **Stack**

   - Simple Stack
   - Min Stack (supports retrieving the minimum element in O(1) time)

2. **Queue**
   - Simple Queue
   - Circular Queue
   - Priority Queue
   - Double-Ended Queue (Deque)

## ⚙️ Key Characteristics

| Feature         | Stack (LIFO)      | Queue (FIFO)             |
| --------------- | ----------------- | ------------------------ |
| Insertion       | `push()`          | `enqueue()`              |
| Deletion        | `pop()`           | `dequeue()`              |
| Access          | Top element only  | Front element only       |
| Time Complexity | O(1) for push/pop | O(1) for enqueue/dequeue |

## 🎯 Common Operations

### Stack Operations

| Operation     | Description                 | Time Complexity |
| ------------- | --------------------------- | --------------- |
| `push(value)` | Add an element to the stack | O(1)            |
| `pop()`       | Remove the top element      | O(1)            |
| `peek()`      | View the top element        | O(1)            |
| `isEmpty()`   | Check if the stack is empty | O(1)            |

### Queue Operations

| Operation        | Description                 | Time Complexity |
| ---------------- | --------------------------- | --------------- |
| `enqueue(value)` | Add an element to the queue | O(1)            |
| `dequeue()`      | Remove the front element    | O(1)            |
| `peek()`         | View the front element      | O(1)            |
| `isEmpty()`      | Check if the queue is empty | O(1)            |

## ✔️ Advantages

- **Stacks**: Simple implementation, useful for recursion and backtracking.
- **Queues**: Efficient for scheduling and managing tasks in order.

## ❌ Disadvantages

- Fixed size if implemented using arrays.
- Limited access to elements (only top for stacks, only front for queues).

## 💡 Example Use Cases

### Stacks

- Function call stack in programming languages.
- Undo/Redo functionality in text editors.
- Expression evaluation and syntax parsing.

### Queues

- Task scheduling in operating systems.
- Breadth-First Search (BFS) in graphs.
- Handling requests in web servers.

## 🎨 Visualization

### Stack (LIFO)

```none
Push: [1] -> [1, 2] -> [1, 2, 3]
Pop:  [1, 2, 3] -> [1, 2] -> [1]
```

### Queue (FIFO)

```none
Enqueue: [1] -> [1, 2] -> [1, 2, 3]
Dequeue: [1, 2, 3] -> [2, 3] -> [3]
```

## 🚀 Implementation

### Stack

```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("Peek from empty stack")

    def is_empty(self):
        return len(self.stack) == 0
```

### Queue

```python
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        raise IndexError("Dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        raise IndexError("Peek from empty queue")

    def is_empty(self):
        return len(self.queue) == 0
```

## 🌐 Language Implementations

### Python

- Stack: Use `list` or `collections.deque`.
- Queue: Use `collections.deque` or `queue.Queue`.

### Java

- Stack: Use `java.util.Stack`.
- Queue: Use `java.util.Queue` or `java.util.LinkedList`.

---

**Key Insight:** Stacks and Queues are essential for solving many algorithmic problems. Understanding their properties and operations is crucial for mastering data structures and algorithms.
