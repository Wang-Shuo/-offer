# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None 
        self.right = None


class Solution:
    def __init__(self):
        self.treeNode = []
    def inOrder(self, pRoot):
        if len(self.treeNode) < 0:
            return None
        if pRoot.left:
            self.inOrder(pRoot.left)
        self.treeNode.append(pRoot)
        if pRoot.right:
            self.inOrder(pRoot.right)
    def KthNode(self, pRoot, k):
        if not pRoot or k == 0:
            return
        self.inOrder(pRoot)
        if len(self.treeNode) < k:
            return None
        return self.treeNode[k - 1]

