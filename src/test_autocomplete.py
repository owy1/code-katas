"""Module to test autocomplete.py."""


import pytest
import os


TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'words.txt')


@pytest.fixture
def small_trie():
    """Fixture for small trie."""
    from autocomplete import AutoCompleter
    vocabulary = ['fix', 'fax', 'fit', 'fist', 'full', 'finch', 'final', 'finial', 'find', 'fine', 'file']
    complete_me = AutoCompleter(vocabulary)
    return complete_me


def test_autocomplete_f(small_trie):
    """Autocomplete "f"."""
    print(set((small_trie.autocomplete('f'))))


def test_autocomplete_fi(small_trie):
    """Autocomplete "fi"."""
    print(set((small_trie.autocomplete('fi'))))


def test_autocomplete_fin(small_trie):
    """Autocomplete "fin".."""
    assert set(['find', 'finial', 'finch', 'final', 'fine']) == set((small_trie.autocomplete('fin')))


def test_autocomplete_finally(small_trie):
    """Autocomplete "finally".."""
    assert (small_trie.autocomplete('finally')) == []


def test_autocomplete_file():
    """Autocomplete read from file."""
    from autocomplete import AutoCompleter
    t = AutoCompleter(TESTDATA_FILENAME)
    assert t.size == 235886
    assert t.contains('abdominal') is True
    assert t.contains('unactually') is True
    assert set(t.autocomplete('aa')) == set(['aalii', 'aal', 'aam', 'aardvark', 'aardwolf'])
    assert set(t.autocomplete('aa', 3)) == set(['aalii', 'aal', 'aam'])


def test_autocomplete(small_trie):
    """Test input error."""
    with pytest.raises(TypeError):
        small_trie.autocomplete(19)
