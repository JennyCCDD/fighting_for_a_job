# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    有效的数独

    # 数字 1-9 在每一行只能出现一次。
    # 数字 1-9 在每一列只能出现一次。
    # 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
@revise log:
    2021.01.09 创建程序
                解题思路：
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 遍历数独
        # (1)同一个数字，所在的行计数加１，如果满足数独特性，计数最多不会大于１
        # (2)同一个数字，所在的列计数加１，如果满足数独特性，计数最多不会大于１
        # (3)同一个数字，所在的九宫格计数加１，如果满足数独特性，计数最多不会大于１。

        ################################################
        # row =[[x for x in y if x !='.']for y in board]
        # col =[[x for x in y if x !='.']for y in zip(*board)]
        # pal =[[board[i+m][j+n]for m in range(3) for n in range(3) if board[i+m][j+n]!='.']for i in (0,3,6)for j in (0,3,6)]
        #
        # return all(len(set(x))==len(x) for x in (*row,*col,*pal))
        ################################################

        # 官方题解
        # init data
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3

                    # keep the current cell value
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True



solution = Solution()
result = solution.isValidSudoku([
["8","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
])
print(result)