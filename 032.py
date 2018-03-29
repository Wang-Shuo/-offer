# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def PrintFromTopToBottom(self, root):
        if not root:
            return

        queue = []
        result = []
        queue.append(root)
        while len(queue) > 0:
            pNode = queue.pop(0)
            result.append(pNode.val)
            if pNode.left:
                queue.append(pNode.left)
            if pNode.right:
                queue.append(pNode.right)

        return result


# test
root = TreeNode(8)
node1 = TreeNode(6)
node2 = TreeNode(10)
node3 = TreeNode(5)
node4 = TreeNode(7)
node5 = TreeNode(9)
node6 = TreeNode(11)
root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6
s = Solution()
print(s.PrintFromTopToBottom(root))
