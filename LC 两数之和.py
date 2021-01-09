# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    两数之和

@revise log:
    2021.01.09 创建程序
                解题思路：
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum = []
        for index_i,i in enumerate(nums):
            for index_j, j in enumerate(nums):
                if index_i < index_j:
                    if target == nums[index_i] + nums[index_j]:
                        sum.append([index_i,index_j])
        return sum[0]


solution = Solution()
result = solution.twoSum(nums = [2,7,11,15], target = 9)
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
print(result)