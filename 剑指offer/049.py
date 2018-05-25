# -*- coding: utf-8 -*-
class Solution:
    def GetUglyNumber(self, index):
        if index <= 0:
            return 0

        uglyNumbers = [1] * index
        nextUglyIndex = 1

        index2 = 0
        index3 = 0
        index5 = 0

        while nextUglyIndex < index:
            minValue = min(uglyNumbers[index2] * 2, uglyNumbers[index3] * 3, uglyNumbers[index5] * 5)
            uglyNumbers[nextUglyIndex] = minValue

            while uglyNumbers[index2] * 2 <= uglyNumbers[nextUglyIndex]:
                index2 += 1
            while uglyNumbers[index3] * 3 <= uglyNumbers[nextUglyIndex]:
                index3 += 1
            while uglyNumbers[index5] * 5 <= uglyNumbers[nextUglyIndex]:
                index5 += 1
            
            nextUglyIndex += 1

        return uglyNumbers[-1]


# test 
s = Solution()
print(s.GetUglyNumber(1))
print(s.GetUglyNumber(0))
print(s.GetUglyNumber(1500))