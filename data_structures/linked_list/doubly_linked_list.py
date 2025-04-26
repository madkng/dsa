class DoublyNode:
    """
    Represents a node in a doubly linked list.

    A doubly linked list differs from a singly linked list in that each node
    contains a pointer to both the next node and the previous node, allowing
    traversal in both directions.
    """

    def __init__(self, val: int, next=None, prev=None):
        """
        Initializes a new node in the doubly linked list.

        Args:
            val (int): The value stored in the node.
            next (DoublyNode, optional): The next node in the list. Defaults to None.
            prev (DoublyNode, optional): The previous node in the list. Defaults to None.
        """
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        """
        Returns a string representation of the node's value.
        """
        return str(self.val)


def display_list(head: DoublyNode):
    """
    Displays the elements of the doubly linked list in order.

    Args:
        head (DoublyNode): The head node of the list.
    """
    curr = head
    elements = []

    while curr:
        elements.append(str(curr.val))
        curr = curr.next

    print(" <-> ".join(elements))


def insert_at_beginning(head: DoublyNode, tail: DoublyNode, val: int):
    """
    Inserts a new node at the beginning of the doubly linked list.

      Args:
          head (DoublyNode): The current head of the list.
          tail (DoublyNode): The current tail of the list.
          val (int): The value to insert.

    Returns:
          tuple: The updated head and tail of the list.
    """
    new_node = DoublyNode(val, next=head)
    head.prev = new_node
    return new_node, tail


def insert_at_end(head: DoublyNode, tail: DoublyNode, val: int):
    """
    Inserts a new node at the end of the doubly linked list.

    Args:
        head (DoublyNode): The current head of the list.
        tail (DoublyNode): The current tail of the list.
        val (int): The value to insert.

    Returns:
        tuple: The updated head and tail of the list.
    """
    new_node = DoublyNode(val, prev=tail)
    tail.next = new_node
    return head, new_node


if __name__ == "__main__":
    HEAD = TAIL = DoublyNode(0)
    display_list(HEAD)

    HEAD, TAIL = insert_at_beginning(head=HEAD, tail=TAIL, val=5)
    display_list(HEAD)

    HEAD, TAIL = insert_at_end(HEAD, TAIL, 10)
    display_list(HEAD)
