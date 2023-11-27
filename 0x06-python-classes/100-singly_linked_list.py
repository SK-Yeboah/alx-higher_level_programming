#!/usr/bin/python3
class Node:
    """
    The Node class represents a node of a singly linked list.

   
    Methods:
        __init__(self, data, next_node=None): Initializes a new instance of the Node class.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Args:
            data (int): Data of the node.
            next_node (Node or None): Next node in the list (default is None).
]
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")

        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")

        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        """Property to retrieve the data of the node."""
        return self._data

    @data.setter
    def data(self, value):
        """
        Property setter to set the data of the node.

        Raises:
            TypeError: If the new value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Property to retrieve the next node in the list."""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """
        Property setter to set the next node in the list.

        Raises:
            TypeError: If the new value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object or None")
        self._next_node = value


class SinglyLinkedList:
    """
    The SinglyLinkedList class represents a singly linked list.
    """
    def __init__(self):
        """Initializes a new instance of the SinglyLinkedList class."""
        self._head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Args:
            value (int): Value of the new Node.

        Raises:
            TypeError: If the provided value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")

        new_node = Node(value)

        if self._head is None or value < self._head.data:
            new_node.next_node = self._head
            self._head = new_node
        else:
            current = self._head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Converts the linked list to a string for printing.

        Returns:
            str: A string representation of the linked list.
        """
        result = ""
        current = self._head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip()
