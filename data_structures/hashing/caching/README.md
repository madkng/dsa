# Caching in Computer Science

**Caching** is a technique used in computer science to store frequently accessed data in a temporary storage area (called a cache) so that future requests for that data can be served faster. Caching is fundamental for improving the performance and efficiency of systems, applications, and networks.

## 🧱 What is a Cache?

A **cache** is a small, fast memory or storage layer that holds copies of data from slower storage or computation sources. When a program or system needs data, it first checks the cache:
- If the data is found (**cache hit**), it is returned quickly.
- If the data is not found (**cache miss**), it is fetched from the original source and often stored in the cache for future use.

## 🔗 How Caching Relates to Hashing

Hashing is a key technique used in implementing efficient caches:
- **Hash functions** map data (such as keys, queries, or addresses) to specific locations in the cache.
- **Hash tables** are commonly used as the underlying data structure for caches, enabling O(1) average time complexity for lookups, insertions, and deletions.

For example, when caching the results of expensive computations or database queries, a hash table can quickly determine if the result is already cached.

## ⚙️ Why Use Caching?

- **Speed**: Accessing data from a cache is much faster than recomputing or retrieving it from the original source.
- **Efficiency**: Reduces redundant computations and network/database calls.
- **Scalability**: Helps systems handle more requests by reducing load on slower resources.

## 🎯 Common Applications of Caching

- **Web Browsers**: Store web pages, images, and scripts for faster loading.
- **Databases**: Cache query results to speed up repeated queries.
- **Operating Systems**: Use CPU caches and disk caches to speed up memory and file access.
- **APIs and Web Servers**: Cache responses to reduce backend load.
- **Content Delivery Networks (CDNs)**: Cache static content closer to users.

## 🧩 Cache Replacement Policies

Since cache storage is limited, old or less-used data must be removed to make space for new data. Common cache replacement policies include:
- **LRU (Least Recently Used)**: Removes the data that has not been used for the longest time.
- **LFU (Least Frequently Used)**: Removes the data used least often.
- **FIFO (First In, First Out)**: Removes the oldest data in the cache.

## 🚀 Example: Simple Cache Using Hashing

```python
class SimpleCache:
    def __init__(self):
        self.cache = {}

    def get(self, key):
        return self.cache.get(key, None)

    def put(self, key, value):
        self.cache[key] = value

# Usage
cache = SimpleCache()
cache.put("user:1", {"name": "Alice"})
result = cache.get("user:1")  # Fast lookup using hashing
```

## ✔️ Advantages

- Dramatically improves performance for repeated data access.
- Reduces latency and resource usage.
- Simple to implement using hash tables.

## ❌ Disadvantages

- Cache can become stale if underlying data changes.
- Limited by cache size (requires eviction policies).
- May add complexity to system design.

---

**Key Insight:**  
Caching is a powerful optimization that relies heavily on hashing for fast data retrieval. Understanding how caches work and how hashing enables efficient cache operations is essential for building high-