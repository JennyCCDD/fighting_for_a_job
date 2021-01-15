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
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        slow = head
        fast = dummy

        for i in range(n):
            slow = slow.next

        while slow:
            slow = slow.next
            fast = fast.next

        fast.next = fast.next.next
        return dummy.next


solution = Solution()
result = solution.removeNthFromEnd([1,2,3,4,5],2)
print(result)

