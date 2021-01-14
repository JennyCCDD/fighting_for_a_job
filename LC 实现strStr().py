# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    实现strStr()
@revise log:
    2021.01.14 创建程序
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ans = -1
        length = len(needle)
        index = 0
        while index < len(haystack):
            if haystack[index:index+length] == needle:
                ans = index
                break
            index += 1
        if needle == "":
            ans = 0
        return ans

solution = Solution()
result = solution.strStr(haystack = "aaa", needle = "a")
print(result)