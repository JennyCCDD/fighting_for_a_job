# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    将有序数组转化为二叉搜索树
@revise log:
    2021.02.09 创建程序
    一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

    中序遍历，总是选择中间位置右边的数字作为根节点
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution {
#     public TreeNode sortedArrayToBST(int[] nums) {
#         return helper(nums, 0, nums.length - 1);
#     }
#
#     public TreeNode helper(int[] nums, int left, int right) {
#         if (left > right) {
#             return null;
#         }
#
#         // 总是选择中间位置右边的数字作为根节点
#         int mid = (left + right + 1) / 2;
#
#         TreeNode root = new TreeNode(nums[mid]);
#         root.left = helper(nums, left, mid - 1);
#         root.right = helper(nums, mid + 1, right);
#         return root;
#     }
# }

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(left,right):
            if left > right:
                return None
            mid = (left + right + 1) / 2

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
        return helper(0,int(len(nums)-1))