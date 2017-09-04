# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# !/usr/bin/env python
# -*- coding: utf-8 -*-


def longest_substring(s):
    """Brute force, time complexity O(n), space complexity O(1)."""

    longest, start, visited = 0, 0, [False for _ in range(256)]
    for idx, char in enumerate(s):
        # import pdb; pdb.set_trace()
        if visited[ord(char)]:
            while char != s[start]:
                visited[ord(s[start])] = False
                start += 1 #increment of initial substring
            start += 1 #increment another substring
        else:
            visited[ord(char)] = True

        longest = max(longest, idx - start + 1)
    return longest

if __name__ == '__main__':  # pragma: no cover
    # s = "abcabcbb" # "abc", length 3
    # s = "bbbbb"  # "b", length 1
    s = "pwwkew" #wke", length 3
    print(longest_substring(s))