# -*- coding:utf-8 -*-
from functools import cmp_to_key

class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers or len(numbers) <= 0:
            return ''
        
        num2str = list(map(str, numbers))

        key = cmp_to_key(lambda x, y: int(x + y) - int(y + x))
        num2str.sort(key = key)
        return ''.join(num2str)


# test 
s = Solution()
print(s.PrintMinNumber([3, 32, 321]))
print(s.PrintMinNumber([23, 1, 0]))