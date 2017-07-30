"""Module for autocomplete."""


import os


class AutoCompleter:
    """Trie data structure."""

    def __init__(self, iterable=None):
        """Init declaration."""
        self.value = None
        self._size = 0
        self.root = self
        self.children = {}
        self.end = False

        if not isinstance(iterable, list):
            if iterable is not None and os.path.isfile(iterable):
                with open(iterable) as f:
                    lines = f.readlines()
                iterable = [x.strip() for x in lines]

        if type(iterable) in [list, tuple, str]:
            for item in iterable:
                self.insert(item)

    def insert(self, string):  # pragma: no cover
        """Insert a word."""
        if string is None or type(string) is not str:
            raise TypeError('wrong input')

        current_node = self.root
        for char in string:
            if char not in current_node.children:
                current_node.children[char] = AutoCompleter()
                current_node.children[char].value = char
            current_node = current_node.children[char]
        if string:
            current_node.end = True
            self._size += 1

    def contains(self, string):  # pragma: no cover
        """Return True if the string is in trie, False if not."""
        if string is None or type(string) is not str:
            raise TypeError('wrong input')
        current_node = self.root
        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
        return current_node.end

    @property
    def size(self):
        """Return size of trie."""
        return self._size

    def traversal(self, start):
        """Return a generator that will return the values in the trie using depth-first traversal, one at a time."""
        current_node = self.children
        for char in current_node:
            for word in current_node[char].traversal(start + char):
                yield word
        if self.end:
            yield start

    def autocomplete(self, start, max_completions=5):
        """Autocomplete."""
        if start is None or type(start) is not str:
            raise TypeError('wrong input')
        current_node = self.root

        for char in start:
            if char in current_node.children:
                current_node = current_node.children[char]

            else:
                return []
        return list(current_node.traversal(start))[:max_completions]

    @property
    def list_words(self):  # pragma: no cover
        """Pre-order traversal to print words in trie in list."""
        result = []
        curr_word = ''
        self._list_words(self.root, curr_word, result)
        return result

    def _list_words(self, node, curr_word, result):  # pragma: no cover
        if node is None:
            return
        for key, child in node.children.items():
            if child.end:
                result.append(curr_word + key)
            self._list_words(child, curr_word + key, result)


if __name__ == '__main__':  # pragma: no cover
    # keyes = ['harp', 'error', 'err', 'erupt', 'suburbia', 'suburban', 'suburb', 'hard', 'harmony', 'may', 'mayor', 'harmonist']
    # keyes = ['fax', 'fix', 'fox', 'fit', 'fist', 'full', 'finch', 'final', 'finial', 'find', 'file']
    TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'words.txt')
    t = AutoCompleter(TESTDATA_FILENAME)
    print(t.size)
    print(t.contains('abdominal'))
    print(t.contains('unactually'))
    print(list(t.autocomplete('aa')))
