# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, sum):
        if not root:
            return []
        if not root.left and not root.right:
            if root.val == sum:
                return [[root.val]]
            else:
                return []

        paths = self.pathSum(root.left, sum - root.val) + self.pathSum(root.right,
                                                                  sum - root.val)
        return [[root.val] + p for p in paths]


# test
root = TreeNode(10)
node1 = TreeNode(5)
node2 = TreeNode(12)
node3 = TreeNode(4)
node4 = TreeNode(7)

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4

s = Solution()
print(s.pathSum(root, 22))


