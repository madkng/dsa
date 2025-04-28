"""
This script demonstrates the implementation and usage of a stack data structure
using Python's built-in list. A stack is a linear data structure that operates
on the Last In, First Out (LIFO) principle, where the last element added is the
first one to be removed.
Key operations demonstrated in this script:
- Initializing an empty stack.
- Adding elements to the stack using the `append` method (push operation).
- Removing the top element from the stack using the `pop` method.
- Viewing the top element of the stack without removing it using indexing.
- Checking if the stack is non-empty using a conditional statement.
Time complexities of operations:
- Push (`append`): O(1)
- Pop (`pop`): O(1)
- Peek (`stk[-1]`): O(1)
- Check if stack is non-empty (`if stk`): O(1)

This script serves as an example of how to use a list as a stack and perform
basic stack operations.

A stack is a linear data structure that follows the Last In, First Out (LIFO) principle.
This means that the last element added to the stack will be the first one to be removed.
Stacks are commonly used in various applications such as:

- Function call management in programming (call stack).
- Undo mechanisms in text editors.
- Expression evaluation and syntax parsing.
- Depth-first search (DFS) in graph algorithms.

Key operations of a stack:
- `push`: Add an element to the top of the stack.
- `pop`: Remove and return the top element of the stack.
- `peek` or `top`: View the top element without removing it.
- `is_empty`: Check if the stack is empty.
- `size`: Get the number of elements in the stack.

This module provides an implementation of the stack and its associated operations.
"""

if __name__ == "__main__":
    # This is a way of implementing a stack as a dynamic array
    # However, it can be implemented as a linked list also
    stk = []  # Stacks - Last In First Out
    print(stk)

    # Append to top of stack - O(1)
    stk.append(5)
    stk.append(4)
    stk.append(3)

    print(stk)

    # Pop from stack - O(1)
    x = stk.pop()

    print(x)
    print(stk)

    # Ask what's on the top of stack - O(1)
    print(stk[-1])

    # As if something is in the stack - O(1)
    if stk:
        print(True)
