# -*- coding: utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        self.stack.append(node)
        if self.minStack == [] or node < self.min():
            self.minStack.append(node)
        else:
            self.minStack.append(self.min())

    def pop(self):
        if self.stack == [] or self.minStack == []:
            return None
        self.minStack.pop()
        self.stack.pop()

    def min(self):
        return self.minStack[-1]


# test
s = Solution()
s.push(3)
s.push(4)
s.push(2)
s.push(1)
print(s.min())
s.pop()
print(s.min())
s.pop()
print(s.min())
