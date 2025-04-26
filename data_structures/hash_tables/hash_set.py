# Hashset
"""
This script demonstrates the usage of Python's built-in `set` data structure,
which implements a hash set. It provides examples of common operations
performed on a hash set, including adding, removing, and checking for
membership of elements, as well as constructing a set from a string and
iterating over its elements.
Usage:
  Run the script directly to see the output of the operations.
Functions and Operations:
  - Create an empty set.
  - Add items to the set using `add()` (O(1) operation).
  - Check if an item exists in the set using the `in` keyword (O(1) operation).
  - Remove items from the set using `remove()` (O(1) operation).
  - Construct a set from a string, which removes duplicate characters
    and retains only unique ones (O(s), where s is the length of the string).
  - Iterate over the elements of the set (O(n), where n is the number of elements in the set).

Notes:
  - Sets are unordered collections of unique elements.
  - All operations on sets are optimized for performance using hash tables.
  - Attempting to remove an element that does not exist in the set using `remove()`
    will raise a `KeyError`. Use `discard()` if you want to avoid this.
"""
if __name__ == "__main__":
    s = set()
    print(s)

    # Add item into Set - O(1)
    s.add(1)
    s.add(2)
    s.add(3)
    print(s)

    # Lookup if item in set - O(1)
    if 1 in s:
        print(True)

    # Remove item from set - O(1)
    s.remove(3)
    print(s)

    string = (
        "aaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccceeeeeeeeeee"
    )
    sett = set(string)  # Set constructuion - O(s) - S is the length of the string

    print(sett)

    # Loop over items in set - O(n)
    for x in s:
        print(x)
