# -*- coding:utf-8 -*-
class Solution:
    def NumOf1(self, n):
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += 1
            n = (n - 1) & n
        return count

    def NumberOf1(self, n):
        if n < 0:
            s = bin(n & 0xffffffff)
        else:
            s = bin(n)
        return s.count('1')


    def PowerOf2(self, n):
        if n & (n - 1) == 0:
            return True
        else:
            return False

    def MToN(self, m, n):
        diff = m^n
        count = 0
        while diff:
            count += 1
            diff = diff & (diff - 1)
        return count

# test
s = Solution()
print(s.NumOf1(1))
print(s.NumOf1(3))
print(s.NumOf1(-1))
print(s.NumOf1(-2))
print(s.PowerOf2(64))
print(s.MToN(10, 13))
