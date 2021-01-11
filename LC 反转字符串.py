# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    反转字符串
    编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
    不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
    你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

@revise log:
    2021.01.11 创建程序
                解题思路：双指针
"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        slow = 0
        fast = len(s)-1
        while slow < fast:
            ####################################
            s[fast], s[slow]  = s[slow], s[fast]
            ####################################
            slow +=1
            fast -=1

        return s

solution = Solution()
result = solution.reverseString(["h","e","l","l","o"])
print(result)