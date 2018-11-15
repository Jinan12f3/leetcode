# -*- coding: utf-8 -*-

"""
leetcode 第35题 搜索插入位置
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if nums:

            for i, num in enumerate(nums):
                if target <= num:
                    return i

                if i == len(nums) - 1:
                    return i + 1

        return 0
