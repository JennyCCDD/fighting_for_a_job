# -*- coding: utf-8 -*-
"""
@author: Mengxuan Chen
@description:
    删除链表的倒数第N个节点

@revise log:
    2021.01.15 创建程序
    2021.01.16 解题思路：
# """

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# In[]
# 方法一：暴力解法
# 首先从头节点开始对链表进行一次遍历，得到链表的长度 L。
# 随后我们再从头节点开始对链表进行一次遍历，当遍历到第 L-n+1L−n+1 个节点时，它就是我们需要删除的节点。

class Solution:
    def removeNthFromEnd(self, head, n):
        def getLength(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        dummy = ListNode(0, head)
        length = getLength(head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next

# In[]
# 方法二：快慢指针
# 关键字：倒数第N个
# 快指针到链表的最后，慢指针与其距离为n+1，删除慢指针的后继节点
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        # step1: 快指针先走n步
        slow, fast = dummy, dummy
        for _ in range(n):
            fast = fast.next

            # step2: 快慢指针同时走，直到fast指针到达尾部节点，此时slow到达倒数第N个节点的前一个节点
        while fast and fast.next:
            slow, fast = slow.next, fast.next

            # step3: 删除节点，并重新连接
        slow.next = slow.next.next
        return dummy.next

# In[]
# 方法三：递归迭代
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            self.count = 0
            return head
        head.next = self.removeNthFromEnd(head.next, n) # 递归调用
        self.count += 1 # 回溯时进行节点计数
        return head.next if self.count == n else head

solution = Solution(object = [1,2,3,4,5])
result = solution.removeNthFromEnd(head = [1,2,3,4,5], n =2)
print(result)

