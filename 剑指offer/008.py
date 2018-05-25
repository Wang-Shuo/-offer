# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def GetNext(self, pNode):
        if pNode == None:
            return
        pNext = None
        if pNode.right:
            pRight = pNode.right
            while pRight.left:
                pRight = pRight.left
            pNext = pRight
        elif pNode.parent:
            pCurrent = pNode
            pParent = pNode.parent
            while pParent and pCurrent == pParent.right:
                pCurrent = pParent
                pParent = pParent.parent
            pNext = pParent
        return pNext
