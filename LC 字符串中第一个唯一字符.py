# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    字符串中第一个唯一字符

@revise log:
    2021.01.11 创建程序
                解题思路：唯一字符 首次出现索引 = 该字符最后出现索引
"""
import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dct = collections.Counter(s)
        # collections.Counter() 快速设置哈希表，其中value的值是每个key出现的次数
        for i, c in enumerate(s):
            if dct[c] == 1:
                return i
        return -1


        #########################################
        # 超出时间限制
        #########################################
        # s_list = list(s)
        #
        # for i, ch in enumerate(s):
        #     if s_list.count(s_list[i]) == 1:
        #         return i
        # return -1

        #########################################
        # 超出时间限制
        #########################################
        # s_list = list(s)
        # index = 0
        # while index < len(s_list):
        #     if s_list.count(s_list[index]) == 1:
        #         output = index
        #         break
        #     else:
        #         output = -1
        #     index += 1
        # return output
        #########################################

solution = Solution()
result = solution.firstUniqChar("loveleedcode")
print(result)