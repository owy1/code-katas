"""Docstring for sort_cards module."""


dic = {'A': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12}


class Task(object):  # pragma: no cover
    """."""

    def __init__(self, val=None, priority=None):
        """Initize Task."""
        self.priority = priority
        self.val = val
        self.head = None
        self.next = None

    def __lt__(self, other):
        """Greater than, may not use."""
        return (self.val, self.priority, ) < (other.val, other.priority)

    @property
    def printList(self):
        """."""
        return self.val, self.priority


class Priorityq(object):  # pragma: no cover
    """Priority Queue data structure."""

    def __init__(self, data=None):
        """Initializer for the class instance."""
        self._length = 0
        self.priorityq = []
        if type(data) is tuple:
            for item in data:
                self.insert(item[0], item[1])

    @property
    def display(self):
        """."""
        print(self.priorityq)

    def pop(self):
        """Remove and return highest priority element from queue."""
        if not self.priorityq:
            raise IndexError('Cannot pop from an empty list.')
        peekpop = min(self.priorityq, key=lambda k: k[1])
        popped = self.priorityq.pop(self.priorityq.index(peekpop))
        self._length -= 1
        return popped

    def insert(self, val, priority):
        """Insert a new value in queue."""
        new_task = Task(val, priority)
        self.head = new_task
        self.priorityq.append((new_task.val, new_task.priority))
        self._length += 1

    @property
    def size(self):
        """Return the length of queue."""
        return self._length

    def peek(self):
        """Return highest priority element in queue without remove."""
        if not self.priorityq:
            raise IndexError('Cannot pop from an empty list.')
        popidx = [y[0] for y in self.priorityq].index(0)
        return self.priorityq[popidx]


def sort_cards(cards):
    """Sort cards by rank."""
    p = Priorityq()
    for card in cards:
        p.insert(card, dic[card])
    ls = [p.pop()[0] for i in range(p.size)]
    return ls

"""
def sort_cards(cards):
    return sorted(cards, key="A23456789TJQK".index)

def sort_cards(cards):

 dic={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13}
 return sorted(cards,key=lambda a:dic[a])

 """
