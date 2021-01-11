# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    整数反转
    假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。
    请根据这个假设，如果反转后整数溢出那么就返回 0。

@revise log:
    2021.01.11 创建程序
                解题思路：将整数转化为字符串进行处理，并考虑边界条件
                执行用时：36 ms, 在所有 Python 提交中击败了19.12%的用户
                内存消耗：13 MB, 在所有 Python 提交中击败了48.88%的用户
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_string = list(str(abs(x)))
        new = 0
        for index, item in enumerate(x_string):
            new += int(x_string[len(x_string)-index-1]) * 10 ** (len(x_string)-index-1)
        if x > 0:
            pass
        else:
            new = -new
        if abs(new)> 2**31-1:
            new = 0
        return new

solution = Solution()
result = solution.reverse(123)
print(result)