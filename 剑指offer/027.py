# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def MirrorRecursively(self, pRoot):
        if not pRoot:
            return
        if not pRoot.left and not pRoot.right:
            return

        pTemp = pRoot.left
        pRoot.left = pRoot.right
        pRoot.right = pTemp

        if pRoot.left:
            self.MirrorRecursively(pRoot.left)
        if pRoot.right:
            self.MirrorRecursively(pRoot.right)



#test
pRoot1 = TreeNode(8)
pRoot2 = TreeNode(6)
pRoot3 = TreeNode(10)
pRoot4 = TreeNode(5)
pRoot5 = TreeNode(7)
pRoot6 = TreeNode(9)
pRoot7 = TreeNode(11)
pRoot1.left = pRoot2
pRoot1.right = pRoot3
pRoot2.left = pRoot4
pRoot2.right = pRoot5
pRoot3.left = pRoot6
pRoot3.right = pRoot7

s = Solution()
s.MirrorRecursively(pRoot1)
print(pRoot1.left.val)
print(pRoot1.right.val)
print(pRoot3.left.val)
print(pRoot3.right.val)
print(pRoot2.left.val)
print(pRoot2.right.val)

