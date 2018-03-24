# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        return self.Symmetrical(pRoot, pRoot)

    def Symmetrical(self, pRoot1, pRoot2):
        if not pRoot1 and not pRoot2:
            return True

        if not pRoot1 or not pRoot2:
            return False

        if pRoot1.val != pRoot2.val:
            return False

        return self.Symmetrical(pRoot1.left, pRoot2.right) and self.Symmetrical(pRoot1.right, pRoot2.left)


# test
pRoot = TreeNode(8)
node1 = TreeNode(6)
node2 = TreeNode(6)
node3 = TreeNode(5)
node4 = TreeNode(7)
node5 = TreeNode(7)
node6 = TreeNode(5)

pRoot.left = node1
pRoot.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6

s = Solution()
print(s.isSymmetrical(pRoot))

