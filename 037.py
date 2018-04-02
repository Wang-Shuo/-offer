# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    flag = -1

    def Serialize(self, root):
        if not root:
            return '#'

        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)


    def Deserialize(self, s):
        self.flag += 1
        l = s.split(',')
        if self.flag >= len(s):
            return None

        root = None
        if l[self.flag] != '#':
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root


# test
# root = TreeNode(1)
# node1 = TreeNode(2)
# node2 = TreeNode(3)
# node3 = TreeNode(4)
# node4 = TreeNode(5)
# node5 = TreeNode(6)

# root.left = node1
# root.right = node2
# node1.left = node3
# node2.left = node4
# node2.right = node5

s = Solution()
# print(s.Serialize(root))
ss = '1,2,4,#,#,#,3,5,#,#,6,#,#'
root = s.Deserialize(ss)
print(s.Serialize(root))