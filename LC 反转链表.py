# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    反转链表
    进阶: 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

@revise log:
    2021.01.16 创建程序
    2021.01.17 解题思路：
# """

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while (curr != None):
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next

        return prev
