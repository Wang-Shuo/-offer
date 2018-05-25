# -*- coding: utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        if not numbers or len(numbers) < 1:
            return False

        numbers.sort()
        numOfZero, numOfGap = 0, 0

        for num in numbers:
            if num == 0:
                numOfZero += 1
        
        small = numOfZero
        big = small + 1
        while big < len(numbers):
            if numbers[small] == numbers[big]:
                return False
            numOfGap += numbers[big] - numbers[small] - 1
            small = big
            big += 1

        if numOfGap > numOfZero:
            return False
        else:
            return True


# test
s = Solution()
print(s.IsContinuous([0, 1, 3, 4, 5]))
print(s.IsContinuous([0, 4, 6, 8, 9]))
