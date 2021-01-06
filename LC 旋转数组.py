# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    旋转数组
    https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2skh7/
@revise log:
    2021.01.06 创建程序
"""
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        nums[0:] = nums[length-k:]+nums[:length-k]
solution = Solution()
result = solution.rotate([1,2,3,4,5,6,7],3)
print(result)


