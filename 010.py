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

    # 青蛙一次可以跳1级或者2级台阶
    def jumpFloor(self, n_floors):
        result = [1, 2]
        if n_floors >= 3:
            for i in range(3, n_floors+1):
                result[(i + 1) % 2] = result[0] + result[1]
            return result[(n_floors + 1) % 2]

    # 青蛙一次可以跳1级到n级台阶
    def jumpFloor2(self, n_floors):
        result = 1
        if n_floors >= 2:
            for i in range(1, n_floors):
                result = result * 2
        return result

# test
s = Solution()
print(s.Fibonacci(2))
print(s.Fibonacci(4))
print(s.jumpFloor(3))
print(s.jumpFloor2(3))
