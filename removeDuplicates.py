# -*- coding: utf-8 -*-

"""
leetcode算法库第26题: 删除排序数组中的重复项
要求原地修改，空间复杂度O(1)
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums:
            i = 0
            for j, num in enumerate(nums):
                if j > 0:
                    if num != nums[j - 1]:
                        i += 1
                        nums[i] = num

            return i + 1

        return 0
