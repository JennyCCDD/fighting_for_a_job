# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    二叉树的最大深度
@revise log:
    2021.02.07 创建程序
    节点的左子树只包含小于当前节点的数。
    节点的右子树只包含大于当前节点的数。
    所有左子树和右子树自身必须也是二叉搜索树。
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node,min=float('-inf'),max=float('inf')):
            if not node:
                return True
            if node.val <= min or node.val >= max:
                return False
            if not helper(node.right, node.val, max):
                return False
            if not helper(node.left, min, node.val):
                return False
            return True

        return helper(root)
