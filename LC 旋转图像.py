# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    旋转图像

@revise log:
    2021.01.09 创建程序
                解题思路：
"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # matrix_ = matrix.copy()
        # matrix_[0][2] = matrix[0][0]
        # matrix_[0][0] = matrix[2][0]
        # matrix_[2][0] = matrix[2][2]
        # matrix_[2][2] = matrix[0][2]
        # matrix_[0][1] = matrix[1][0]
        # matrix_[1][0] = matrix[2][1]
        # matrix_[2][1] = matrix[1][2]
        # matrix_[1][2] = matrix[0][1]
        # row = len(matrix)
        # for i in range(row):
        #     for j in range(row):
        #         matrix[row - i - 1][row - j - 1] = matrix[i][j]
        return matrix
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
solution = Solution()
result = solution.rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
])
print(result)

