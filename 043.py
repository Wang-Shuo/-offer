# -*- coding: utf-8 -*-
class Solution:
    # https://leetcode.com/problems/number-of-digit-one/discuss/64381/4-lines-olog-n-cjavapython
    # http://blog.chinaunix.net/uid-30592332-id-5750466.html

    def countDigitOne(self, n):
        ones = 0
        m = 1
        while m <= n:
            a = n // m
            b = n % m
            if a % 10 >= 2:
                ones += (a // 10 + 1) * m
            elif a % 10 == 1:
                ones += a // 10 * m + b + 1
            else:
                ones += a // 10 * m

            m *= 10

        return ones  

# test 
s = Solution()
print(s.countDigitOne(12))
print(s.countDigitOne(0))
print(s.countDigitOne(1))
print(s.countDigitOne(21235))