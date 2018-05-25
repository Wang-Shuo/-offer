# -*- coding: utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def MeetingNode(self, pHead):
        if not pHead:
            return None

        pSlow = pHead.next
        if not pSlow:
            return None

        pFast = pSlow.next
        while pFast and pSlow:
            if pFast == pSlow:
                return pFast

            pSlow = pSlow.next
            pFast = pFast.next
            if pFast:
                pFast = pFast.next

        return None

    def EntryNodeOfLoop(self, pHead):
        meetingNode = self.MeetingNode(pHead)

        if not meetingNode:
            return None

        nodesInLoop = 1
        pNode1 = meetingNode
        while pNode1.next != meetingNode:
            pNode1 = pNode1.next
            nodesInLoop += 1

        pNode1 = pHead
        for i in range(nodesInLoop):
            pNode1 = pNode1.next

        pNode2 = pHead
        while pNode1 != pNode2:
            pNode1 = pNode1.next
            pNode2 = pNode2.next

        return pNode1


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
node5.next = node3

print(s.EntryNodeOfLoop(node1).val)
