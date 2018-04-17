# -*- coding: utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, string):
        fdict = {}
        order = []
        for c in string:
            if c in fdict:
                fdict[c] += 1
            else:
                fdict[c] = 1
                order.append(c)

        for c in order:
            if fdict[c] == 1:
                return c


# test 
s = Solution()
print(s.FirstNotRepeatingChar('abaccdeff'))