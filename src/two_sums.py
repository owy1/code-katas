# https://leetcode.com/problems/two-sum/solution/
# !/usr/bin/env python
# -*- coding: utf-8 -*-


def two_sums(nums, target):
    """Brute force, time complexity O(n**2), space complexity O(1)."""
    temp_ls = sorted([i for i in nums if i < target])
    temp = temp_ls[0]
    temp_ls = temp_ls[1:]
    ls = [i for i in temp_ls if i + temp == target]
    ls.insert(0, temp)
    return ls

if __name__ == '__main__':  # pragma: no cover
    nums, target = [2, 7, 11, 15], 9
    print(two_sums(nums, target)) #[2,7]