# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    字符串转换整数
@revise log:
    2021.01.14 创建程序
    首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：
    如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
    假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
    该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
    假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。
    在任何情况下，若函数不能进行有效的转换时，请返回 0 。
"""
INT_MAX=2**31-1
INT_MIN=-2**31

class Automata:
    def __init__(self):
        self.state="start"
        self.ans=0
        self.sign=1
        self.table={
            "start":["start","sign","innum","end"],
            "sign":["end","end","innum","end"],
            "innum":["end","end","innum","end"],
            "end":["end","end","end","end"],
        }
    def get_s(self,c):
        if c.isspace():
            return 0
        if c=='+' or c=='-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self,c):
        self.state=self.table[self.state][self.get_s(c)]
        if self.state=="innum":
            self.ans=self.ans*10+int(c)
            self.ans= min(self.ans,INT_MAX) if self.sign==1 else min(self.ans,-INT_MIN)
        if self.state=="sign":
            if c=='-':
                sign=-1


import re
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 解法1：
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i = i + 1
        if n == 0 or i == n:
            return 0
        flag = 1
        if s[i] == '-':
            flag = -1
        if s[i] == '+' or s[i] == '-':
            i = i + 1
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        ans = 0
        while i < n and '0' <= s[i] <= '9':
            ans = ans * 10 + int(s[i]) - int('0')
            i += 1
            if (ans - 1 > INT_MAX):
                break

        ans = ans * flag
        if ans > INT_MAX:
            return INT_MAX
        return INT_MIN if ans < INT_MIN else ans

        # 解法2，官方题解：有限状态机
        # Auto = Automata()
        # for c in s:
        #     Auto.get(c)
        # return Auto.ans * Auto.sign

        # 解法3.正则表达式
        # 正则表达式通常被用来测试字符串内的模式、替换那些符合某个模式的文本、基于模式匹配从字符串中提取子字符串。
        # return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2 ** 31 - 1), -2 ** 31)

solution = Solution()
result = solution.myAtoi("4193 with words")
print(result)