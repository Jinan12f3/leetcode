# -*- coding: utf-8 -*-

"""
leetcode 第22题 括号生成
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        matches = list()

        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n:
                matches.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)

        backtrack()
        return matches
