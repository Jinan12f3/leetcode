# -*- coding: utf-8 -*-

"""
leetcode算法库第39题: 组合总和
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # 存储不重复匹配组合
        matches = list()

        def search(match, cs, tg):

            for i in cs:

                new_match = match[:]
                new_match.append(i)

                if sum(new_match) == tg:
                    new_match = sorted(new_match)
                    if new_match not in matches:
                        matches.append(new_match)
                elif sum(new_match) < tg:
                    search(new_match, cs, tg)
                else:
                    continue

        search([], candidates, target)

        if matches:
            return list(matches)

        return []
