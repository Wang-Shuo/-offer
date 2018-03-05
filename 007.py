# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def reConstructBinaryTree(self, preorder, inorder):
        if len(preorder) == 0 and len(inorder) == 0:
            return None

        if set(preorder) != set(inorder):
            return None

        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        root.left = self.reConstructBinaryTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.reConstructBinaryTree(preorder[idx+1:], inorder[idx+1:])

        return root

# test
preorder = [1, 2, 4, 7, 3, 5, 6, 8]
inorder = [4, 7, 2, 1, 5, 3, 8, 6]
s = Solution()
reTree = s.reConstructBinaryTree(preorder, inorder)
print(reTree.left.val, reTree.right.val)
print(reTree.val)
