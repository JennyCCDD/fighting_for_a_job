# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    爬楼梯
@revise log:
    2021.02.12 创建程序
                解题思路：
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 时间复杂度太高，超时了
        # if n <= 2:
        #     return n
        # return  self.climbStairs(n - 1) + self.climbStairs(n - 2)

        if n <= 3:
            return n

        f1, f2, f3 = 1, 2, 0

        for i in range(3, n + 1, 1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
            i += 1
        return f3

