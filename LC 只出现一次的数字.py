# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    只出现一次的数字
    https://leetcode-cn.com/problems/single-number/
@revise log:
    2021.01.06 创建程序
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            if nums.count(i) == 1:
                x = i
        return x

solution = Solution()
result = solution.singleNumber([4,1,2,1,2])
print(result)