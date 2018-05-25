# -*- coding: utf-8 -*- 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        nLength1 = self.GetListLength(pHead1)
        nLength2 = self.GetListLength(pHead2)
        nLengthDiff = abs(nLength1 - nLength2)

        if nLength2 > nLength1:
            pListHeadLong = pHead2
            pListHeadShort = pHead1
        else:
            pListHeadLong = pHead1
            pListHeadShort = pHead2

        for i in range(nLengthDiff):
            pListHeadLong = pListHeadLong.next

        while pListHeadLong and pListHeadShort and pListHeadLong != pListHeadShort:
            pListHeadLong = pListHeadLong.next
            pListHeadShort = pListHeadShort.next

        pFirstCommonNode = pListHeadLong

        return pFirstCommonNode


    def GetListLength(self, pHead):
        nLength = 0
        pNode = pHead
        while pNode:
            nLength += 1
            pNode = pNode.next
        
        return nLength


# test 


