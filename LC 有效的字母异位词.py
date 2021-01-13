# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    有效的字母异位词
@revise log:
    2021.01.13 创建程序
"""
import collections
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dct_s = collections.Counter(s)
        dct_t = collections.Counter(t)
        if dct_s == dct_t:
            x = 1
        else:
            x = 0
        return bool(x)

solution = Solution()
result = solution.isAnagram( s = "rat", t = "car")
    # s = "anagram", t = "nagaram")
print(result)


