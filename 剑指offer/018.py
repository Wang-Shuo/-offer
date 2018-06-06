# -*- coding: utf-8 -*-
class ListNode:
    def __init__(self, x = None):
        self.val = x
        self.next = None
    def __del__(self):
        self.val = None
        self.next = None


class Solution:
    def DeleteNode(self, pListHead, pToBeDeleted):
        if not pListHead or not pToBeDeleted:
            return

        if pToBeDeleted.next != None:
            pNext = pToBeDeleted.next
            pToBeDeleted.val = pNext.val
            pToBeDeleted.next = pNext.next
            pNext.__del__()
        elif pListHead == pToBeDeleted:
            pToBeDeleted.__del__()
            pListHead.__del__()
        else:
            pNode = pListHead
            while pNode.next != pToBeDeleted:
                pNode = pNode.next
            pNode.next = None
            pToBeDeleted.__del__()


    def DeleteDuplication(self, pHead):
        if not pHead:
            return

        pPreNode = None
        pNode = pHead
        while pNode != None:
            pNext = pNode.next
            needDelete = False
            if pNext != None and pNext.val == pNode.val:
                needDelete = True

            if not needDelete:
                pPreNode = pNode
                pNode = pNode.next
            else:
                value = pNode.val
                pToBeDel = pNode
                while pToBeDel != None and pToBeDel.val == value:
                    pNext = pToBeDel.next
                    pToBeDel = pNext
                if pPreNode == None:
                    pHead = pNext
                else:
                    pPreNode.next = pNext
                pNode = pNext

        return pHead


# test
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4

s = Solution()
s.DeleteNode(node1, node2)
print(node2.val)
s.DeleteNode(node1, node4)
print(node4.val)
s.DeleteNode(node1, node1)
print(node1.val)

# s = Solution()
# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(2)
# node4 = ListNode(3)
# node5 = ListNode(3)
# node6 = ListNode(4)
# node7 = ListNode(5)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# node5.next = node6
# node6.next = node7

# pHead = s.DeleteDuplication(node1)
# while pHead:
#     print(pHead.val)
#     pHead = pHead.next
