"""
Least Recently Used (LRU) Cache is a data structure that stores a limited number of items and evicts
the least recently used item when the limit is reached.

It is commonly used in scenarios where memory is limited,
and we want to keep the most frequently accessed items.

The LRU Cache is implemented using a combination of a
hash map (dictionary) and a doubly linked list.

This allows for O(1) time complexity for both access and insertion operations.

The hash map stores the items with their keys for quick access,
while the doubly linked list maintains the order of usage.

When an item is accessed, it is moved to the front of the list,
indicating that it is the most recently used.

When the cache reaches its limit, the least recently used 
item (the one at the back of the list) is removed to make space for new items.
"""

from typing import Any


class Node:
    """
    A class representing a node in a doubly linked list.
    Each node contains a key, data, and pointers to the previous and next nodes.
    This is used to maintain the order of usage in the LRU Cache.
    """
    def __init__(self, key: Any, data:Any):
        self.key = key
        self.data = data
        self.prev:Node = None
        self.next:Node = None

class LRUCache:
    """
    A class representing a Least Recently Used (LRU) Cache.
    It uses a combination of a hash map and a doubly linked list to achieve O(1) time complexity for
    both get and put operations.
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # Dictionary to store key and node mapping
        self.head = Node(None, None) # Dummy head node
        self.tail = Node(None, None) # Dummy tail node
        self.head.next = self.tail # Initialize the doubly linked list
        self.tail.prev = self.head # Initialize the doubly linked list

    def _del_node(self, node: Node):
        """Delete a node from the doubly linked list"""
        # Unlink the node from its neighbors
        prev_node = node.prev
        next_node = node.next

        # Update the pointers of the neighboring nodes
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_node(self, node: Node):
        """Add a node right after the head node"""

        # Get the current next node of the head
        next_node = self.head.next

        # Update the pointers to insert the new node
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def get(self, key: Any) -> Any:
        """Get the value of the key if it exists in the cache, otherwise return -1"""
        if key not in self.cache:
            return -1

        # Move the accessed node to the front (most recently used)
        node = self.cache[key]
        self._del_node(node)
        self._add_node(node)

        return node.data

    def put(self, key: Any, value: Any) -> None:
        """Insert or update the value of the key in the cache"""

        # If the key already exists, update the value and move it to the front
        if key in self.cache:
            #  Remove the old node from the cache and the linked list
            node = self.cache[key]
            self._del_node(node)
            del self.cache[key]

        # If the cache is at capacity, remove the least recently used item
        if len(self.cache) >= self.capacity:

            # Remove the node before the tail (the least recently used item)
            lru_node = self.tail.prev
            self._del_node(lru_node)
            del self.cache[lru_node.key]

        # Create a new node for the key-value pair
        new_node = Node(key, value)

        # Add the new node to the front of the linked list
        self._add_node(new_node)
        # Add the new node to the cache
        self.cache[key] = new_node

    def __repr__(self):
        """String representation of the cache for debugging"""
        items = []
        current = self.head.next
        while current != self.tail:
            items.append(f"{current.key}: {current.data}")
            current = current.next
        return "LRUCache([" + ", ".join(items) + "])"

# Example usage
if __name__ == "__main__":
    lru_cache = LRUCache(2)
    lru_cache.put(1, 'A')
    lru_cache.put(2, 'B')
    print(lru_cache.get(1))  # Output: 'A'
    lru_cache.put(3, 'C')     # Evicts key 2
    print(lru_cache.get(2))  # Output: -1 (not found)
    lru_cache.put(4, 'D')     # Evicts key 1
    print(lru_cache.get(1))  # Output: -1 (not found)
    print(lru_cache.get(3))  # Output: 'C'
    print(lru_cache.get(4))  # Output: 'D'
    print(lru_cache)          # Output: LRUCache([3: C, 4: D])
