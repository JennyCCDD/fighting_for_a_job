# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    二叉树的层序遍历
@revise log:
    2021.02.08 创建程序

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




# 广度优先搜索 Breath First Search
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/tao-mo-ban-bfs-he-dfs-du-ke-yi-jie-jue-by-fuxuemin/
# 如果不需要确定当前遍历到了哪一层，BFS模板如下。

# while queue 不空：
#     cur = queue.pop()
#     for 节点 in cur的所有相邻节点：
#         if 该节点有效且未访问过：
#             queue.push(该节点)

# 2. 如果要确定当前遍历到了哪一层，BFS模板如下。
# level = 0
# while queue 不空：
#     size = queue.size()
#     while (size --) {
#         cur = queue.pop()
#         for 节点 in cur的所有相邻节点：
#             if 该节点有效且未被访问过：
#                 queue.push(该节点)
#     }
#     level ++;

import collections
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # deque是双端队列（double-ended queue）的缩写，由于两端都能编辑，
        # deque既可以用来实现栈（stack）也可以用来实现队列（queue）。
        # https://www.cnblogs.com/lincappu/p/12890765.html
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)
        return res



