# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    删除排序数组中的重复项
    https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2gy9m/
@revise log:
    2021.01.05 创建程序
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        while j < len(nums)-1:
            j += 1
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

solution = Solution()#[0, 1, 2, 3, 4]
result = solution.removeDuplicates([0,0,0,1,1,1,2,2,3,3,4])
print(result)
