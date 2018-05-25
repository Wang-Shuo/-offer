# -*- coding: utf-8 -*-
class Solution:
    def digitAtIndex(self, index):
        if index < 0:
            return -1

        digits = 1
        while True:
            if digits == 1:
                numbers = 10
            else:
                numbers = 9 * 10 ** (digits - 1)

            if index < numbers * digits:
                return self.digitAtIndexFinal(index, digits)
            
            index -= digits * numbers
            digits += 1

    def digitAtIndexFinal(self, index, digits):
        digitBeginNumber = 0 if digits == 1 else 10 ** (digits - 1)
        number = digitBeginNumber + index // digits
        idxInNumber = index % digits
        return int(str(number)[idxInNumber])


# test 
s = Solution()
print(s.digitAtIndex(10))
print(s.digitAtIndex(1001))
print(s.digitAtIndex(0))
print(s.digitAtIndex(1))