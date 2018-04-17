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


class Solution2:
    def __init__(self):
        self.s = ""
    
    def FirstNotRepeatingChar(self):
        array = list(self.s)
        for c in array:
            if array.count(c) == 1:
                return c
        return '#'

    def Insert(self, char):
        self.s += char


# test 
s = Solution()
print(s.FirstNotRepeatingChar('abaccdeff'))