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

    def IsBalanced(self, pRoot):
        if not pRoot:
            return True
        
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        diff = left - right
        if diff > 1 or diff < -1:
            return False

        return self.IsBalanced(pRoot.left) and self.IsBalanced(pRoot.right)


class Solution2:
    def IsBalanced(self, pRoot):
        return self._is_balanced(pRoot)[0]

    def _is_balanced(self, pRoot):
        if not pRoot:
            return (True, 0)

        left = self._is_balanced(pRoot.left)
        right = self._is_balanced(pRoot.right)
        if left[0] and right[0]:
            diff = left[1] - right[1]
            if abs(diff) <= 1:
                return (True, max(left[1], right[1]) + 1)

        return (False, max(left[1], right[1]) + 1)


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
print(s.IsBalanced(pRoot))
s2 = Solution2()
print(s2.IsBalanced(pRoot))