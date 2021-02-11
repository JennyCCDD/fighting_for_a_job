# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    第一个错误的版本
@revise log:
    2021.02.10 创建程序
"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if not isBadVersion(mid - 1) and isBadVersion(mid):
                return mid
            elif isBadVersion(mid + 1) and not isBadVersion(mid):
                return mid + 1
            elif isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1

        # left = 1
        # right = n
        # while (left < right):
        #     mid = left + (right - left) / 2
        # if (isBadVersion(mid)):
        #     right = mid
        # else:
        #     left = mid + 1
        # return left

        # i = int( n / 2 )
        # while i < n:
        #     if ( isBadVersion(i) == False) and ( isBadVersion(i+1) == True):
        #         return int( n / 2 )+1
        #     if ( isBadVersion(i) == False) and ( isBadVersion(i+1) == False):
        #         i = int( i / 2)
        #     if ( isBadVersion(i) == True) and ( isBadVersion(i+1) == True):
        #         i = int(n/2) + int(i/2)

