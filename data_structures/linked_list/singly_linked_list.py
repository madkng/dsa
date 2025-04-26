class Node:
    """
    Represents a node in a singly linked list.

    A singly linked list is a data structure where each node contains a value
    and a reference (or pointer) to the next node in the sequence.
    """

    def __init__(self, val: int, next: "Node" = None):
        """
        Initializes a new node in the singly linked list.

        Args:
            val (int): The value stored in the node.
            next (Node, optional): The next node in the list. Defaults to None.
        """
        self.val = val
        self.next = next

    def __str__(self):
        """
        Returns:
            str: A string representation of the node's value.
        """
        return str(self.val)


def display_list(head: Node):
    """
    Displays the elements of the singly linked list in order.

    Args:
        head (Node): The head node of the list.

    Time Complexity:
        O(n): Traverses the entire list to collect and display all elements.
    """
    curr = head
    elements = []

    # Traverse the list and collect node values
    while curr:
        elements.append(str(curr.val))
        curr = curr.next

    # Print the list in a readable format
    print(" -> ".join(elements))


def search_for_node(head: Node, target: int) -> bool:
    """
    Searches for a node with a specific value in the singly linked list.

    Args:
        head (Node): The head node of the list.
        target (int): The value to search for.

    Returns:
        bool: True if the value is found, False otherwise.

    Time Complexity:
        O(n): Traverses the list to search for the target value.
    """
    curr = head

    # Traverse the list to find the target value
    while curr:
        if target == curr.val:
            return True
        curr = curr.next

    return False


if __name__ == "__main__":
    # Create nodes for the singly linked list
    HEAD = Node(1)
    A = Node(3)
    B = Node(4)
    C = Node(7)

    # Link the nodes to form the list
    HEAD.next = A
    A.next = B
    B.next = C

    # Display the list
    print("Singly Linked List:")
    display_list(head=HEAD)

    # Search for a value in the list
    target_value = 2
    print(
        f"\nIs {target_value} in the list? {search_for_node(head=HEAD, target=target_value)}"
    )
