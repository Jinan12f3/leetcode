# -*- coding: utf-8 -*-

"""
leetcode 第58题 最后一个单词的长度
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s:
            if " " in s:
                results = s.split(" ")
                if results:
                    for r in results[::-1]:
                        if r:
                            return len(r)
            else:
                return len(s)

        return 0
