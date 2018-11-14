# -*- coding: utf-8 -*-

"""
leetcode算法库第27题: 移除元素
要求原地修改，空间复杂度O(1)
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        if nums:
            for i in range(nums.count(val)):
                nums.remove(val)
            return len(nums)

        return 0
