# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    最大子序和
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
        pre = 0
        maxnums = nums[0]
        for i in nums:
            pre = max(pre + i, i)
            maxnums = max(maxnums, pre)
        return maxnums

        # 我的第一种写法，超出时间限制
        # n = len(nums)
        # if n == 0: return 0  # 边界条件
        # if n == 1: return nums[0]
        # dp = [0] * n
        #
        # for i in range(1, n+1):
        #     ddp = [0] * i
        #     if len(range(i)) == 1: ddp[0]=nums[-1]
        #     for j in range(i):
        #         ddp[j] = sum(nums[i-1-j:i])
        #     dp[i-1] = max(ddp)
        # return max(dp)

solution = Solution()
result = solution.maxSubArray([-2,1])
print(result)