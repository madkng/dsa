"""A simple implementation of a binary search tree (BST) in Python.
This code defines a Node class that represents a node in the binary search tree.
Each node contains a value, and references to its left and right children.
The class provides methods to insert new values, check for the presence of a value,
display the tree structure, and print the values in ascending order."""

class Node:
    """
    Class representing a node in a binary search tree.

    Attributes:
        value (int): The value stored in the node.
        left (Node or None): Reference to the left child node.
        right (Node or None): Reference to the right child node.

    Methods:
        insert(value):
            Inserts a new value into the binary search tree according to BST rules.
        contains(value):
            Checks if the binary search tree contains a specified value.
        display(level=0):
            Displays the binary search tree in a structured, indented format.
        ordered_print():
            Prints the values of the binary search tree in ascending order using in-order traversal.
    """

    def __init__(self, value: int):
        self.left = None
        self.right=None
        self.value=value

    def insert(self, value):
        """
        Inserts a new value into the binary search tree.
        If the value is less than the current node's value, it goes to the left subtree
        If the value is greater than or equal to the current node's value, it goes to
        """
        if value < self.value:
            if self.left is None:
                self.left = Node(value=value)

            else:
                self.left.insert(value)

        else:
            if self.right is None:
                self.right = Node(value=value)

            else:
                self.right.insert(value)

    def contains(self, value):
        """
        Checks if the binary search tree contains a value.
        Returns True if the value is found, otherwise returns False."""
        if value == self.value:
            return True

        elif value < self.value:
            if self.left is None:
                return False

            else:
                return self.left.contains(value)

        else:
            if self.right is None:
                return False

            else:
                return self.right.contains(value)

    def display(self, level=0):
        """
        Displays the binary search tree in a structured format.
        The right subtree is displayed above the current node,
        and the left subtree is displayed below.
        Each level of the tree is indented by 4 spaces.
        This helps visualize the structure of the tree.
        """
        if self.right is not None:
            self.right.display(level + 1)

        print(' ' * 4 * level + '->', self.value)

        if self.left is not None:
            self.left.display(level + 1)

    def ordered_print(self):
        """
        Prints the values of the binary search tree in ascending order.
        This is done by performing an in-order traversal of the tree.
        """
        if self.left is not None:
            self.left.ordered_print()

        print(self.value)

        if self.right is not None:
            self.right.ordered_print()

if __name__ == "__main__":
    root = Node(value=10)
    root.insert(5)
    root.insert(15)
    root.insert(8)


    root.display()
    print(root.contains(7))
    print(root.contains(15))
    root.ordered_print()
