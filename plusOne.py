# -*- coding: utf-8 -*-

"""
leetcode 第66题 加一
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        s = ''
        for i in [str(n) for n in digits]:
            s += i

        result = list(str(int(s) + 1))
        return [int(r) for r in result]
