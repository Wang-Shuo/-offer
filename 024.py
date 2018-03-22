# -*- coding: utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def ReverseList(self, pHead):
        pReversedHead = None
        pNode = pHead
        pPrev = None

        while pNode:
            pNext = pNode.next
            if not pNext:
                pReversedHead = pNode

            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext

        return pReversedHead

    def ReverseListRecursively(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        else:
            pReversedHead = self.ReverseListRecursively(pHead.next)
            pHead.next.next = pHead
            pHead.next = None
        return pReversedHead


# test
s = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print(s.ReverseList(node1).val)
print(node5.next.val)
#print(s.ReverseListRecursively(node1).val)
#print(node5.next.val)
