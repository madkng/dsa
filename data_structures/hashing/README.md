# Hashing Data Structure

Hashing is a technique used to uniquely identify a specific object from a group of similar objects. It refers to the process of generating a fixed-size output (hash code or hash value) from an input of typically large and variable size, using mathematical formulas known as hash functions. Hashing is fundamental in computer science for efficient data retrieval, storage, and security.

## 🧱 Basic Structure

A typical hashing system consists of:

- **Key**: The input value (can be a string, number, etc.) to be stored or retrieved.
- **Hash Function**: A mathematical function that converts the key into a hash code (an integer).
- **Hash Table**: An array-like data structure that stores values at positions determined by the hash code.

```python
# Example: Simple hash table using Python dictionary
hash_table = {}
hash_table["apple"] = 5
hash_table["banana"] = 7
```

## 🔄 When Not to Use Hashing

- When you need to maintain sorted data (use self-balancing BSTs).
- When string keys require prefix search (use Trie).
- When you need floor/ceiling operations (use BSTs).

## ⚙️ Key Components

1. **Key**: The data to be stored or searched.
2. **Hash Function**: Maps the key to an index in the hash table.
3. **Hash Table**: Stores the data at the computed index.

## 🔑 Key Characteristics

- **Fast access**: Average-case O(1) time for search, insert, and delete.
- **No ordering**: Data is not stored in any particular order.
- **Efficient memory usage**: Only stores what is needed, but can waste space if poorly sized.

## 🎯 Common Operations

| Operation | Description                | Time Complexity (Avg) |
|-----------|----------------------------|----------------------|
| Insert    | Add a key-value pair       | O(1)                 |
| Search    | Find value by key          | O(1)                 |
| Delete    | Remove key-value pair      | O(1)                 |

## 💡 How Hashing Works

Suppose we have a set of strings {"ab", "cd", "efg"} to store in a table of size 7.

1. Assign values to characters: "a"=1, "b"=2, etc.
2. Compute sum of characters: "ab"=3, "cd"=7, "efg"=18.
3. Hash function: `sum(string) % 7`
   - "ab" → 3 % 7 = 3
   - "cd" → 7 % 7 = 0
   - "efg" → 18 % 7 = 4

## 🛠️ Applications of Hashing

- **Databases**: Indexing for fast lookup.
- **Compilers**: Symbol tables.
- **Caching**: Fast access to frequently used data.
- **Cryptography**: Password storage, digital signatures.
- **Networking**: Routing tables, packet checksums.
- **Data Deduplication**: Detecting duplicate files.
- **Load Balancing**: Distributing requests evenly.

## 🧩 Collision Handling Techniques

When two keys hash to the same index, a **collision** occurs. Common techniques to handle collisions:

1. **Chaining**: Store multiple elements at the same index using a linked list or another data structure.
   ```python
   # Example: Chaining using a list of lists
   hash_table = [[] for _ in range(7)]
   hash_table[3].append("ab")
   hash_table[0].append("cd")
   ```
2. **Open Addressing**: Find another open slot using a probing sequence.
   - **Linear Probing**: Check next slot sequentially.
   - **Quadratic Probing**: Check slots at intervals of i^2.
   - **Double Hashing**: Use a second hash function to determine the step size.

## 📏 Load Factor and Rehashing

- **Load Factor**: Ratio of number of elements to table size.
  - Load Factor = (Number of elements) / (Table size)
  - High load factor increases collisions; low load factor wastes space.
- **Rehashing**: When load factor exceeds a threshold (commonly 0.75), resize the table (usually double) and re-insert all elements.

## ✔️ Advantages

- Very fast average-case access, insert, and delete.
- Efficient for large datasets.
- Flexible key types (strings, numbers, etc.).

## ❌ Disadvantages

- No ordering of elements.
- Poor hash functions can cause many collisions and degrade performance.
- Not suitable for range queries or prefix searches.

## 🚀 Implementation Example

```python
class HashTable:
    def __init__(self, size=7):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return sum(ord(c) for c in str(key)) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))

    def search(self, key):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

    def delete(self, key):
        idx = self._hash(key)
        self.table[idx] = [(k, v) for k, v in self.table[idx] if k != key]
```

## 🌐 Language Implementations

### Python

- Use built-in `dict` for hash tables.
- Use `set` for hash sets.

### Java

- Use `HashMap`, `HashSet` in `java.util`.

---

**Key Insight:**  
Hashing is a cornerstone of efficient data storage and retrieval. Understanding hash functions, collision handling, and load factor is essential for designing robust and high-performance applications.