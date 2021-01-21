# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    合并两个有序列表

@revise log:
    2021.01.21 创建程序
               解题思路：
# """

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 解法一：（非o(1)空间复杂度解法）
        # 遍历链表，每次遍历到一个新的结点时，判断该结点是否在集合set中，如果在集合set中说明链表有环，
        # 否则记录在set(集合)中，继续遍历。

        # if head is None:
        #     return False
        # node = head
        # nodeset = set()
        # while (node):
        #     if node in nodeset:
        #         return True
        #     else:
        #         nodeset.add(node)
        #     node = node.next
        # return False
        ##################################################
        # 解法2：快慢指针
        if head is None:
            return False
        fastnode = head
        slownode = head
        while (fastnode):
            if fastnode.next and fastnode.next.next:
                fastnode = fastnode.next.next
                slownode = slownode.next
            else:
                return False

            if fastnode == slownode:
                return True
        return False




