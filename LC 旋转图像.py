# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    旋转图像
    https://leetcode-cn.com/problems/rotate-image/

@revise log:
    2021.01.09 创建程序
                解题思路：原地旋转，使用临时变量temp防止原地旋转被覆盖
                时间复杂度：O(N^2)O(N 2 )，其中 NN 是 \textit{matrix}matrix 的边长。我们需要枚举的子矩阵大小为 O(\lfloor n/2 \rfloor \times \lfloor (n+1)/2 \rfloor) = O(N^2)⌊n/2⌋×⌊(n+1)/2⌋)=O(N 2)。
                空间复杂度：O(1)O(1)。为原地旋转。

"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        for i in range(int(row/2)):
            for j in range(int((row+1)/2)):
                temp = matrix[i][j]
                matrix[i][j]=matrix[row-j-1][i]
                matrix[row-j-1][i]=matrix[row-i-1][row-j-1]
                matrix[row-i-1][row-j-1]=matrix[j][row-i-1]
                matrix[j][row-i-1]=temp

        return matrix

solution = Solution()
result = solution.rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
])
print(result)