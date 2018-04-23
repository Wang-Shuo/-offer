# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None 
        self.right = None

class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0

        nLeft = self.TreeDepth(pRoot.left)
        nRight = self.TreeDepth(pRoot.right)

        if nLeft > nRight:
            return nLeft + 1
        else:
            return nRight + 1


# test 
pRoot = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(5)
node5 = TreeNode(6)
node6 = TreeNode(7)

pRoot.left = node1
pRoot.right = node2
node1.left = node3
node1.right = node4
node2.right = node5
node4.left = node6

s = Solution()
print(s.TreeDepth(pRoot))