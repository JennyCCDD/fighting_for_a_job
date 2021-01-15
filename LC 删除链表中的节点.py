# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    删除链表中的节点

    链表至少包含两个节点。
    链表中所有节点的值都是唯一的。
    给定的节点为非末尾节点并且一定是链表中的一个有效节点。
    不要从你的函数中返回任何结果。

@revise log:
    2021.01.15 创建程序
                解题思路：
# """
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def __init__(self, x):
        self.val = x
        self.next = None

    def deleteNode(self):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        self.val = self.next.val
        self.next = self.next.next



# head = [4,5,1,9], node = 5
solution = Solution([4,5,1,9])
result = solution.deleteNode(node = 5)
print(result)
