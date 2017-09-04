# https://leetcode.com/problems/add-two-numbers/solution/
# !/usr/bin/env python
# -*- coding: utf-8 -*-


class Node(object):
    """."""

    def __init__(self, data=None):
        """."""
        self.data = data
        self.next = None

    def display(self):
        """."""
        current = self
        while current:
            print(current.data) if hasattr(current, "data") else None
            current = current.next

    def _tolist(self):
        """."""
        current = self
        previous = None
        ls = []
        while current:
            next, current.next, previous = current.next, previous, current
            ls.append(current.data)
            current = next
        return list(reversed(ls[1:]))


def createlist(nodelist):
    """."""
    head = Node(nodelist[0])
    tail = head

    for i in range(1, len(nodelist)):
        temp = Node(nodelist[i])
        tail.next = temp
        tail = temp
    return head
    # reverse the linklist order
    # head = Node(nodelist[-1])
    # nodelist = nodelist[:-1]
    # tail = head

    # for i in reversed(nodelist):
    #     temp = Node(i)
    #     tail.next = temp
    #     tail = temp
    # return head

def add_two_nums(l1, l2):
    """."""
    tail = Node()
    current, carry = tail, 0
    head = current
    while l1 or l2:

        val = carry
        if l1:
            val += l1.data
            l1 = l1.next
        if l2:
            val += l2.data
            l2 = l2.next
        carry, val = val // 10, val % 10

        current.next = Node(val)
        current = current.next
    if carry == 1:
        current.next = Node(1)

    return head


if __name__ == '__main__':  # pragma: no cover
    l1, l2 = [3, 4, 2], [4, 6, 5]  #807
    # l1, l2 = [0, 1], [0, 1, 2]
    # l1, l2 = [], [0, 1]
    # l1, l2 = [9, 9], [1]
    a = createlist(l1)
    b = createlist(l2)
    headsum = add_two_nums(a, b)
    c = createlist(headsum._tolist())
    c.display()
