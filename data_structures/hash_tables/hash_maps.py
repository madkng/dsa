if __name__ == "__main__":
    """
    This script demonstrates the usage of hashmaps (dictionaries) and related data structures in Python.
    Features:
    1. Basic dictionary operations:
      - Creating a dictionary.
      - Adding a key-value pair to the dictionary (O(1)).
      - Checking for the presence of a key in the dictionary (O(1)).
      - Accessing the value corresponding to a key in the dictionary (O(1)).
      - Iterating over key-value pairs in the dictionary (O(n)).
    2. Usage of `defaultdict` from the `collections` module:
      - Automatically initializes dictionary values with a default type (e.g., `int`).

    3. Usage of `Counter` from the `collections` module:
      - It stores elements as dictionary keys and their counts as values.
      - It provides convenient methods for common counting tasks, such as finding the most common elements or subtracting counts.

    Modules:
    - `collections.defaultdict`: Provides dictionaries with default values for missing keys.
    - `collections.Counter`: Provides a convenient way to count occurrences of elements in an iterable.

    Example:
    - Demonstrates how to use `defaultdict` to handle missing keys gracefully.
    - Demonstrates how to use `Counter` to count character frequencies in a string.
    """
    # Hashmaps - Dictionaries
    d = {"eugene": 1, "ivan": 2, "steve": 3}
    print(d)

    # Add key:val in dictionary O(1)
    d["arsh"] = 4
    print(d)

    # Check for the presence of key in dictionary: O(1)
    if "eugene" in d:
        print(True)

    # Check the value corresponding to a key in dictionary: O(1)
    print(d["eugene"])

    # Loop over the key:val pairs of the dictionary: O(n)
    for key, val in d.items():
        print(f"key {key}: val {val}")

    # Defaultdict
    from collections import defaultdict

    default = defaultdict(int)

    print(default[2])
    print(default)

    # Count frequency
    from collections import Counter

    string = (
        "aaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccceeeeeeeeeee"
    )
    counter = Counter(string)
    print(counter)
