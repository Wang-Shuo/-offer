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

    def PrintFromTopToBottomInLines(self, root):
        if not root:
            return

        queue = []
        nextLevel = 0
        toBePrinted = 1
        queue.append(root)
        while len(queue) > 0:
            pNode = queue.pop(0)
            print(pNode.val, end=' ')
            if pNode.left:
                queue.append(pNode.left)
                nextLevel += 1
            if pNode.right:
                queue.append(pNode.right)
                nextLevel += 1
            toBePrinted -= 1
            if toBePrinted == 0:
                print(' ')
                toBePrinted = nextLevel
                nextLevel = 0


    def PrintZigZag(self, root):
        if not root:
            return

        result, nodes = [], [root]
        right = True
        while nodes:
            curStack, nextStack = [], []
            if right:
                for node in nodes:
                    curStack.append(node.val)
                    if node.left:
                        nextStack.append(node.left)
                    if node.right:
                        nextStack.append(node.right)
            else:
                for node in nodes:
                    curStack.append(node.val)
                    if node.right:
                        nextStack.append(node.right)
                    if node.left:
                        nextStack.append(node.left)
            nextStack.reverse()
            right = not right
            result.append(curStack)
            nodes = nextStack
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
#s.PrintFromTopToBottomInLines(root)
print(s.PrintZigZag(root))
