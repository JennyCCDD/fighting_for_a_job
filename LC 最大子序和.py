# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    买卖股票的最佳时机
@revise log:
    2021.02.15 创建程序
                解题思路：
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0  # 边界条件
        if n == 1: return nums[0]
        dp = [0] * n

        for i in range(1, n):
            ddp = [0] * i
            for j in range(1,i):
                ddp[j] = sum(nums[i-j:i])
            dp[i] = max(ddp)

        return max(dp)

solution = Solution()
result = solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(result)