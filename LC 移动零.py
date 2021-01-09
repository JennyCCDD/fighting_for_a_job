# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    移动零

@revise log:
    2021.01.09 创建程序
                解题思路：
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for index, item in enumerate(nums):
            if nums[index] == 0:
                nums.remove(nums[index])
                nums.append(0)
        return nums

solution = Solution()
result = solution.moveZeroes([0,1,0,3,12])
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
print(result)