# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    两个数组的交集
    https://leetcode-cn.com/problems/single-number/
@revise log:
    2021.01.06 创建程序
    2021.01.09 运行成功
"""
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        both = set(nums1) & set(nums2)
        both_count = []
        for item in list(both):
            count = min((nums1.count(item)), (nums2.count(item)))
            ###############################
            both_count += [item]* count
            ###############################
        return both_count

solution = Solution()
# result = solution.intersect([1,2,2,1],[2,2])
result = solution.intersect([4,9,5],[9,4,9,8,4])
print(result)