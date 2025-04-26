# Hash Tables: HashMaps & HashSets

A **Hash Table** is a data structure that implements an associative array, mapping keys to values using a hash function. It provides average O(1) time complexity for key operations, making it highly efficient for lookups.

## 🧩 Basic Components

1. **Hash Function**: Converts keys into array indices
2. **Buckets**: Array storage for key-value pairs
3. **Collision Handling**: Strategy to manage key conflicts

```python
# Simple hash table implementation sketch
class HashMap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]  # Using separate chaining

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        bucket = self.buckets[self._hash(key)]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
```

## 🔄 Types of Hash Tables

### 1. HashMaps (Dictionary)

- Stores key-value pairs
- Unique keys with optional null values
- Example: Python `dict`, Java `HashMap`

### 2. HashSets

- Stores unique elements only
- Implements mathematical set operations
- Example: Python `set`, Java `HashSet`

## ⚙️ Key Characteristics

| Feature            | Description                                                         |
| ------------------ | ------------------------------------------------------------------- |
| Average Complexity | O(1) for insert, delete, access                                     |
| Collision Handling | Separate Chaining, Open Addressing (Linear/Quadratic Probing)       |
| Load Factor        | Threshold (typically 0.75) triggering table resizing                |
| Ordering           | Generally unordered (some implementations maintain insertion order) |

## 🎯 Common Operations

### HashMap Operations

| Operation       | Description                  | Time Complexity |
| --------------- | ---------------------------- | --------------- |
| `put(key, val)` | Insert/Update key-value pair | O(1) average    |
| `get(key)`      | Retrieve value by key        | O(1) average    |
| `remove(key)`   | Delete key-value pair        | O(1) average    |
| `containsKey`   | Check key existence          | O(1) average    |

### HashSet Operations

| Operation       | Description             | Time Complexity |
| --------------- | ----------------------- | --------------- |
| `add(value)`    | Insert element          | O(1) average    |
| `remove(value)` | Delete element          | O(1) average    |
| `contains`      | Check element existence | O(1) average    |

## ✔️ Advantages

- Fast average-case access time
- Flexible key types (objects, strings, etc.)
- Dynamic resizing
- Efficient duplicate detection (HashSet)

## ❌ Disadvantages

- Worst-case O(n) time with collisions
- Memory overhead for bucket storage
- Dependent on good hash function quality
- No inherent ordering

## 💡 Example Use Cases

**HashMaps**

- Database indexing
- Caching systems
- Frequency counters
- Configuration storage

**HashSets**

- Duplicate detection
- Membership testing
- Mathematical set operations
- Graph node tracking

## 🎨 Visualization

### Separate Chaining

```none
Index  Bucket Contents
0      [ ]
1      → (key1, val1) → (key2, val2)
2      [ ]
3      → (key3, val3)
```

### Open Addressing

```none
Index  Key-Value Pair
0      (key2, val2)
1      EMPTY
2      (key1, val1)
3      (key3, val3)
```

## 🌐 Language Implementations

### Python

```python
# HashMap equivalent
my_dict = {"apple": 1, "banana": 2}

# HashSet equivalent
my_set = {"apple", "banana"}
```

### Java

```java
// HashMap
Map<String, Integer> map = new HashMap<>();
map.put("apple", 1);

// HashSet
Set<String> set = new HashSet<>();
set.add("apple");
```

## 🚨 Collision Resolution

1. **Separate Chaining**

   - Uses linked lists at each bucket
   - Simple implementation
   - Handles arbitrary collisions

2. **Open Addressing**
   - Linear Probing: Try next sequential index
   - Quadratic Probing: Square number steps
   - Double Hashing: Use secondary hash function

---

**Key Insight:** The efficiency of hash tables depends heavily on:

1. Quality of hash function (uniform distribution)
2. Load factor management (typically keep < 0.7)
3. Collision resolution strategy effectiveness
