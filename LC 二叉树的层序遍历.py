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
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        treelist = []
        def appendall(tree,left,right):
            return [tree,left,right]
        return treelist.append(appendall(root.val,root.left.val,root.right.val))


