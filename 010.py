# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        if n < 0:
            return
        result = [0, 1]
        if n < 2:
            return result[n]

        fibNMinusOne = 1
        fibNMinusTwo = 0
        fibN = 0
        for i in range(2, n+1):
            fibN = fibNMinusOne + fibNMinusTwo

            fibNMinusTwo = fibNMinusOne
            fibNMinusOne = fibN

        return fibN

# test
s = Solution()
print(s.Fibonacci(2))
print(s.Fibonacci(4))
