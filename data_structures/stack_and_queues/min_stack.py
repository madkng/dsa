"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.
"""


class MinStack:
    """
    MinStack is a data structure that supports stack operations with an additional
    functionality to retrieve the minimum element in constant time.
    Attributes:
      values (list): A list to keep track of the stack elements for representation purposes.
    Inner Class:
      Node:
        Represents a node in the stack with the following attributes:
        - x (int): The value of the node.
        - min (int): The minimum value in the stack at the time this node was added.
        - next (Node): A reference to the next node in the stack.
    Methods:
      __init__():
        Initializes an empty MinStack.
      push(val: int) -> None:
        Pushes a new value onto the stack. Updates the minimum value if necessary.
      pop() -> None:
        Removes the top element from the stack.
      top() -> int:
        Returns the value of the top element in the stack.
      getMin() -> int:
        Retrieves the minimum value in the stack.
      __repr__() -> str:
        Returns a string representation of the stack values.
    """

    values = []

    class Node:
        def __init__(self, x: int, min: int, next=None):
            self.x = x
            self.min = min
            self.next = next

    def __init__(self):
        self.HEAD = None

    def push(self, val: int) -> None:
        # If list is empty
        if self.HEAD == None:
            self.HEAD = self.Node(val, val, None)
            self.values.append(str(val))

        else:
            # If not empty, update head
            node = self.Node(val, min(self.HEAD.min, val), self.HEAD)
            self.values.append(str(val))
            self.HEAD = node

    def pop(self) -> None:
        self.values.pop()
        self.HEAD = self.HEAD.next

    def top(self) -> int:
        return self.HEAD.x

    def getMin(self) -> int:
        return self.HEAD.min

    def __repr__(self):
        return str(self.values)


def display_stack(stack: MinStack):
    print("Current stack:")
    print(" << ".join(stack.values))


if __name__ == "__main__":
    stack = MinStack()
    stack.push(10)
    stack.push(11)
    stack.push(12)
    display_stack(stack=stack)

    print(f"Popped: {stack.top()}")
    stack.pop()

    display_stack(stack=stack)
    top = stack.top()
    print("Top: {top}")

    minimum = stack.getMin()
    print(f"Minimum: {minimum}")
