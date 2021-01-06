# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    存在重复元素
    https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x248f5/
@revise log:
    2021.01.06 创建程序
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if  len(set(nums)) < len(nums):
            x = 1
        else:
            x = 0
        return bool(x)
# 超出时间限制
# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         x = 0
#         for index_i,i in enumerate(nums):
#             for index_j,j in enumerate(nums):
#                 if index_i != index_j:
#                     if nums[index_i] == nums[index_j]:
#                         x += 1
#         return bool(x)
solution = Solution()
result = solution.containsDuplicate([1,2,3,1])
print(result)