"""This module takes a unicode string (text) as input and returns values."""

# -*- coding: utf-8 -*-


class Node(object):
    """Docstring for Node."""

    def __init__(self, data=None, next_node=None):
        """Initializer for the class instance."""
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    """Docstring for LinkedList."""

    def __init__(self, data=None):
        """Initializer for the class instance."""
        self.head = None
        self._length = 0

        if type(data) in [list, tuple, str]:
            for item in data:
                self._length += 1
                self.push(item)

        elif data is not None:
            raise TypeError('Requires an iterable value.')

    def push(self, val):
        """Insert val at the head of the list."""
        if not val:
            raise ValueError('You must provide a not-null value.')
        new_node = Node(val, self.head)
        if self.head is None:
            self.head = new_node
        else:
            self.head.next_node = self.head
            self.head = new_node
        self._length += 1

    def pop(self):
        """Pop the head of the list."""
        if not self.head:
            raise IndexError('Cannot pop from an empty list.')
        popped = self.head
        self.head = self.head.next_node
        self._length -= 1
        return popped.data


def balance_parens(text):
    """Take a string and returns values."""
    ll = LinkedList()
    balanced = 0
    idx = 0
    while idx < len(text):
        if text[idx] == ")" and balanced == 0:
            balanced = -1
            break
        elif text[idx] == "(" and balanced >= 0:
            ll.push(text[idx])
            balanced += 1
        else:
            ll.pop()
            balanced -= 1
        idx += 1
    return balanced
