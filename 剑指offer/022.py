# -*- coding: utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if not head or k == 0:
            return None

        pAhead = head
        pBehind = None

        for i in range(k-1):
            if pAhead.next != None:
                pAhead = pAhead.next
            else:
                return None

        pBehind = head
        while pAhead.next != None:
            pAhead = pAhead.next
            pBehind = pBehind.next

        return pBehind


# test
s = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

print(s.FindKthToTail(node1, 2).val)
