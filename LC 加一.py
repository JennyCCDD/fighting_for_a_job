# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    加一
    https://leetcode-cn.com/problems/plus-one/
@revise log:
    2021.01.09 创建程序
                解题思路：把list变为一串数字，数字+1再拆分为字符串。
                        原list前几位数字为0，先算出有几个没有用的0，再最后的字符串里面加进去
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for index, item in enumerate(digits):
            num += digits[index] * 10 ** (len(digits)-index-1)
        plus = num + 1
        plus_list = list(map(int,str(plus)))
        zeros_pre = len(digits) - len(str(num))
        x = 0
        while x < zeros_pre:
            plus_list.insert(0,0)
            x += 1
        return plus_list

solution = Solution()
result = solution.plusOne([0,9,9])
print(result)