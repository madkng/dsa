# LRU (Least Recently Used) Cache Algorithm

The **LRU (Least Recently Used) cache** is a popular caching algorithm used to manage limited storage by keeping the most recently accessed data readily available and discarding the least recently used items when space is needed. LRU is widely used in operating systems, databases, and web browsers to improve performance and resource utilization.

## 🧱 What is LRU Cache?

An **LRU cache** stores a fixed number of items. When the cache is full and a new item needs to be added, the item that has not been accessed for the longest time (the "least recently used") is removed to make space.

## 🔄 How LRU Works

1. **Access**: When data is accessed (read or written), it is marked as the most recently used.
2. **Insert**: If the cache is not full, new data is added. If full, the least recently used item is evicted before adding the new data.
3. **Eviction**: The item that has not been used for the longest time is removed first.

## ⚙️ Typical Implementation

LRU caches are often implemented using:
- A **hash table** for O(1) access to cache items by key.
- A **doubly linked list** to track the order of usage, with the most recently used item at the front and the least recently used at the back.

This combination allows both fast lookups and efficient updates to usage order.

## 🚀 Example: Simple LRU Cache in Python

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

## 🎯 Applications of LRU Cache

- **CPU and memory caches**: Managing recently used instructions or data.
- **Web browsers**: Storing recently visited pages or images.
- **Databases**: Caching query results or disk pages.
- **Operating systems**: Page replacement algorithms in virtual memory.

## ✔️ Advantages

- Simple and effective for many real-world workloads.
- Ensures frequently accessed data stays in cache.
- O(1) time complexity for get and put operations (with proper data structures).

## ❌ Disadvantages

- May not be optimal for all access patterns (e.g., cyclic or random access).
- Slightly more complex to implement than simpler policies like FIFO.

---

**Key Insight:**  
The LRU cache algorithm is a practical and efficient way to manage limited storage by prioritizing recent usage. Understanding LRU is essential for designing high-performance systems that 
prioritize both speed and efficient resource utilization.