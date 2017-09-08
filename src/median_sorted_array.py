# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# !/usr/bin/env python
# -*- coding: utf-8 -*-


def median_sorted_array(A, B):
    """Time complexity O(log (m+n)), space complxity 0(1)."""
    len1, len2 = len(A), len(B)
    if (len1 + len2) % 2 == 1: #odd length
        return getmiddle(A, B, int((len1 + len2) / 2) + 1)
    else:
        return (getmiddle(A, B, int((len1 + len2) / 2)) + getmiddle(A, B, int((len1 + len2) / 2) + 1)) * 0.5


def getmiddle(A, B, k):
    """."""
    len1, len2 = len(A), len(B)
    if len1 > len2:
        return getmiddle(B, A, k)
    left, right = 0, len1
    while left < right:
        mid = left + int((right - left) / 2)
        if 0 <= k - 1 - mid < len2 and A[mid] >= B[k - 1 - mid]:
            right = mid
        else:
            left = mid + 1

    Ai = A[left - 1] if left - 1 >= 0 else float('-inf')
    Bj = B[k - 1 - left] if k - 1 - left >= 0 else float('-inf')
    return max(Ai, Bj)

if __name__ == '__main__':  # pragma: no cover
    # nums1, nums2 = [1, 3], [2] # median is 2
    nums1, nums2 = [1, 2], [3, 4] # median is 2.5
    # nums1, nums2 = [1,3, 5, 7], [2, 4, 6, 8] # median is 4.5
    # nums1, nums2 = [1, 3], [2, 4, 6] # median is 3
    print(median_sorted_array(nums1, nums2))
