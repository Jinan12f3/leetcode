# -*- coding: utf-8 -*-

"""
leetcode算法库第40题: 组合总和II
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # 存储不重复匹配组合
        matches = list()

        def search(match, cs, tg):

            for i, c in enumerate(cs):

                new_match = match[:]
                new_match.append(c)

                if sum(new_match) == tg:
                    new_match = sorted(new_match)
                    if new_match not in matches:
                        matches.append(new_match)
                elif sum(new_match) < tg:
                    ncs = cs[:]
                    ncs.pop(i)
                    search(new_match, ncs, tg)
                else:
                    break

        candidates = sorted(candidates)
        for j, cd in enumerate(candidates):

            if cd == target:
                if [cd] not in matches:
                    matches.append([cd])
            elif cd < target:
                new_cs = candidates[:]
                new_cs.pop(j)
                search([cd], new_cs, target)
            else:
                break

        if matches:
            return list(matches)

        return []
