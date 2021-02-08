# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    对称二叉树
@revise log:
    2021.02.07 创建程序
    给定一个二叉树，检查它是否是镜像对称的。
    你可以运用递归和迭代两种方法解决这个问题吗？
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def helper(node1,node2):
            if node1 is None and node2 is None:
                return True  # 同时为空
            if node1 is None or node2 is None:
                return False  # 一个为空
            if (node1.val != node2.val):# 值不相等 ！！
                return False
            return helper(node1.left,node2.right) and helper(node1.right,node2.left)
        return helper(root.left,root.right)