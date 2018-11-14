# -*- coding: utf-8 -*-

"""
leetcode算法库第28题: 实现strStr()
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle in haystack:

            i = 0
            j = len(needle)
            while i + j <= len(haystack):
                if haystack[i:i + j] == needle:
                    return i

                i += 1

        if haystack == needle or not needle:
            return 0

        return -1
