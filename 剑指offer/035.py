# -*- coding: utf-8 -*-  
class ComplexListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.sibling = None


class Solution:
    def CloneNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = ComplexListNode(0)
            pCloned.val = pNode.val
            pCloned.next = pNode.next
            
            pNode.next = pCloned
            pNode = pCloned.next

    def ConnectSiblingNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = pNode.next
            if pNode.sibling:
                pCloned.sibling = pNode.sibling.next

            pNode = pCloned.next

    def ReconnectNodes(self, pHead):
        pNode = pHead
        if pNode:
            pClonedHead = pClonedNode = pNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next

        while pNode:
            pClonedNode.next = pNode.next
            pClonedNode = pClonedNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next

        return pClonedHead

    def Clone(self, pHead):
        if not pHead:
            return

        self.CloneNodes(pHead)
        self.ConnectSiblingNodes(pHead)
        return self.ReconnectNodes(pHead)


# test 
s = Solution()
node1 = ComplexListNode(1)
node2 = ComplexListNode(2)
node3 = ComplexListNode(3)
node1.next = node2
node2.next = node3
node2.sibling = node1

cloned = s.Clone(node1)
print(cloned.next.sibling.val)