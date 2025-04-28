"""
This script demonstrates the usage of a queue data structure using Python's `collections.deque`.
Key Features:
- A queue is a linear data structure that follows the First In, First Out (FIFO) principle.
- Elements are added to the rear (enqueue) and removed from the front (dequeue).
Operations Demonstrated:
1. Enqueue: Adding elements to the right of the queue using `append()`.
2. Dequeue: Removing elements from the left of the queue using `popleft()`.
3. Peek: Accessing elements from the left or right without removing them.
Performance:
- Enqueue and Dequeue operations using `deque` are O(1).
Usage:
- Task scheduling.
- Breadth-first search (BFS) in graph traversal.
- Managing requests in multi-threaded environments.
Additional Topics to Explore:
- Circular queues: Connects the last position back to the first.
- Priority queues: Dequeues elements based on priority.
- Double-ended queues (deque): Allows adding/removing elements from both ends.
"""

if __name__ == "__main__":
    # Queues - First In First Out
    from collections import deque

    q = deque()
    print(q)

    # Enqueue - Add elements to the right - O(1)
    q.append(5)
    q.append(6)
    q.append(7)
    # Dequeue (pop left) - Remove element from the left - O(1)
    q.popleft()

    # Peek from left side
    print(q[0])

    # Peek from right side
    print(q[-1])
