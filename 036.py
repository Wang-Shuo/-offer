# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRoot):
        pLastNodeInList = None
        lst = [pLastNodeInList]
        self.ConvertNode(pRoot, lst)

        pHeadOfList = lst[0]
        while pHeadOfList != None and pHeadOfList.left != None:
            pHeadOfList = pHeadOfList.left

        return pHeadOfList

    def ConvertNode(self, pNode, lst):
        if not pNode:
            return

        pCurrent = pNode
        if pCurrent.left:
            self.ConvertNode(pNode.left, lst)

        pCurrent.left = lst[0]

        if lst[0]:
            lst[0].right = pCurrent

        lst[0] = pCurrent

        if pCurrent.right:
            self.ConvertNode(pCurrent.right, lst)


# test
root = TreeNode(10)
node1 = TreeNode(6)
node2 = TreeNode(14)
node3 = TreeNode(4)
node4 = TreeNode(8)
node5 = TreeNode(12)
node6 = TreeNode(16)

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6

s = Solution()
pHead = s.Convert(root)
while pHead:
    print(pHead.val, end=' ')
    pHead = pHead.right
