# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    买卖股票的最佳时机
@revise log:
    2021.02.12 创建程序
                解题思路：
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 动态规划
        n = len(prices)
        if n == 0: return 0  # 边界条件
        dp = [0] * n
        minprice = prices[0]

        for i in range(1, n):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - minprice)

        return dp[-1]

        # 我的写法
        # minprice = 10**5
        # maxprofit = 0
        # for i in range(0,len(prices)):
        #     if prices[i] < minprice:
        #         minprice = prices[i]
        #     elif (prices[i] - minprice > maxprofit):
        #         maxprofit = prices[i] - minprice
        #
        # return maxprofit



        # maxprofit = 0;
        # for i in range(0,len(prices)):
        #     for j in range(i+1,len(prices)):
        #         profit = prices[j] - prices[i]
        #         if profit > maxprofit:
        #             maxprofit = profit
        # return maxprofit
