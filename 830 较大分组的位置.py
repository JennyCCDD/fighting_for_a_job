# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    找到较大分组的位置
    https://leetcode-cn.com/problems/positions-of-large-groups/
@revise log:
    2021.01.05 创建程序
    2021.01.06 需要考虑边界条件
"""
# class Solution(object):
#     def largeGroupPositions(self, s):
#         ans = []
#         fast, slow = 0, 0
#         while fast < len(s):
#             # 起始位置相同，慢指针保持不变、快指针移动到连续区间末尾
#             while fast < len(s) and s[slow] == s[fast]:
#                 fast += 1
#             # 判断是否符合“较大分组”
#             if fast - slow >= 3:
#                 ans.append([slow, fast-1])
#             # 从新的区间开始，更新慢指针与快指针
#             slow = fast
#             fast += 1
#         return ans
class Solution(object):
    def largeGroupPositions(self, s):
        ans = []
        start, count = 0, 0
        if len(s) < 2:
            return ans
        for i in range(len(s)-1):
            if s[i] == s[start]:
                count +=1
            else:
                if count >=2:
                    ans.append([start,i])
                start = i
                count = 0
        if count >=2:
            ans.append([start,i+1])
        return ans
solution = Solution()
result = solution.largeGroupPositions("aaa")#"abbxxxxzzy")
print(result)