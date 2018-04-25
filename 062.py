# -*- coding: utf-8 -*-
class Solution:
    def LastRemaining(self, n, m):
        if n < 1 or m < 1:
            return -1
        
        last = 0
        for i in range(2, n + 1):
            last = (last + m) % i

        return last


# test 
s = Solution()
print(s.LastRemaining(5, 3))
