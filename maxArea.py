# -*- coding: utf-8 -*-

"""
leetcode 第11题 盛最多水的容器
使用双指针法实现
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        maxarea = 0
        i = 0
        j = len(height) - 1

        func = lambda x, y: x if x > y else y

        while j - i >= 1:

            if height[i] < height[j]:
                maxarea = func(height[i] * (j - i), maxarea)
                i += 1
            else:
                maxarea = func(height[j] * (j - i), maxarea)
                j -= 1

        return maxarea
