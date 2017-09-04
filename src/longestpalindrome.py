# https://leetcode.com/problems/longest-palindromic-substring/solution/
# !/usr/bin/env python
# -*- coding: utf-8 -*-


def get_palindrome_length(string, index):
    """Return longest palindrome substring center in the given index."""
    length = 1
    while index + length < len(string) and index - length >= 0:
        if string[index + length] == string[index - length]:
            length += 1
        else:
            break
    return length - 1


def interleave(string):
    """Put | in between each alphabet in string."""
    new_string = []
    for s in string:
        new_string.extend(['|',s])
    new_string.append('|') # add | at the end
    return ''.join(new_string)


def manacher(string):
    """."""
    right = 0
    center = 0
    string = interleave(string)
    plengthmax = 0
    P = list(map(lambda e: 0, range(len(string)))) #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for idx in range(1, len(string)):
        mirror = 2 * center - idx
        if idx + P[mirror] <= right and mirror >= len(string) - idx:
            P[idx] = P[mirror]
        else:
            plength = get_palindrome_length(string, idx)
            P[idx] = plength
            if plength > plengthmax: plengthmax = plength
            if plength > 1:
                center = int(idx)
                right = center + plength
    # print("string: ", string)
    # print("P: ", P)
    # print("plengthmax: ", plengthmax)
    # print("plengthmax index: ", P.index(plengthmax))
    # print("string of plenghtmax: ", string[P.index(plengthmax)])
    # rightmax = P.index(plengthmax)+plengthmax 
    ls = []
    for idx in range(P.index(plengthmax)-plengthmax, P.index(plengthmax)+plengthmax):
        if string[idx] != '|':
            ls.append(string[idx])

    return ''.join(ls)


if __name__ == '__main__':  # pragma: no cover
    # string = 'abababa'
    string = 'abaaba'
    # string = 'abcqqqqqqxy'
    print(manacher(string))