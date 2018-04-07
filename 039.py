# -*- coding: utf-8 -*-
class Solution:
    def MoreThanHalfNum(self, numbers):
        length = len(numbers)
        if not numbers or length <= 0:
            return 0
        
        result = numbers[0]
        times = 1
        for i in range(1, length):
            if times == 0:
                result = numbers[i]
                times = 1
            elif numbers[i] == result:
                times += 1
            else:
                times -= 1
        
        if not self.CheckMoreThanHalf(numbers, length, result):
            result = 0
        
        return result

    
    def CheckMoreThanHalf(self, numbers, length, number):
        times = 0
        for i in range(length):
            if numbers[i] == number:
                times += 1
        
        if times * 2 <= length:
            return False
        return True


# test
s = Solution()
print(s.MoreThanHalfNum([1, 2, 3, 2, 2, 2, 5, 4, 2]))
print(s.MoreThanHalfNum([1, 2, 3, 4, 4, 4]))
print(s.MoreThanHalfNum([1, 2, 3]))
