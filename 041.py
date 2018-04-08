# -*- coding: utf-8 -*-
class Solution:
    def __init__(self):
        self.numbers = []
    def Insert(self, num):
        self.numbers.append(num)
        self.numbers.sort()
    def GetMedian(self):
        length = len(self.numbers)
        if length == 0:
            return
        if length & 1 == 0:
            return (self.numbers[length // 2] + self.numbers[length // 2 - 1]) / 2.0
        return self.numbers[length // 2]


# test
s = Solution()
s.Insert(1)
s.Insert(3)
s.Insert(5)
s.Insert(7)
print(s.GetMedian())
