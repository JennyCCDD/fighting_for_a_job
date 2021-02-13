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
        minprice = 10**5
        maxprofit = 0
        for i in range(0,len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif (prices[i] - minprice > maxprofit):
                maxprofit = prices[i] - minprice

        return maxprofit



        # maxprofit = 0;
        # for i in range(0,len(prices)):
        #     for j in range(i+1,len(prices)):
        #         profit = prices[j] - prices[i]
        #         if profit > maxprofit:
        #             maxprofit = profit
        # return maxprofit
