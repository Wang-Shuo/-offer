# -*- coding: utf-8 -*-
class Solution:
    def IsPopOrder(self, pPush, pPop):
        if pPush == [] or pPop == []:
            return False
        stack = []
        for i in pPush:
            stack.append(i)
            while len(stack) and stack[-1] == pPop[0]:
                stack.pop()
                pPop.pop(0)

        if len(stack):
            return False
        else:
            return True


# test
pPush = [1, 2, 3, 4, 5]
pPop = [4, 5, 3, 2, 1]
pPop2 = [4, 5, 2, 1, 3]
s = Solution()
print(s.IsPopOrder(pPush, pPop))
print(s.IsPopOrder(pPush, pPop2))
