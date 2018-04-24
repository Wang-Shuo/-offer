# -*- coding: utf-8 -*-
class Solution:
    def FindNumsAppearOnce(self, numbers):
        if not numbers or len(numbers) < 2:
            return 
        resultExclusiveOR = 0
        for num in numbers:
            resultExclusiveOR ^= num

        indexOf1 = self.FindFirstBitIs1(resultExclusiveOR)

        num1, num2 = 0, 0
        for num in numbers:
            if self.IsBit1(num, indexOf1):
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]

    def FindFirstBitIs1(self, num):
        indexBit = 0
        while num & 1 == 0 and indexBit < 32:
            num = num >> 1
            indexBit += 1

        return indexBit

    def IsBit1(self, num, indexBit):
        num = num >> indexBit
        return (num & 1)


    def FindNumberAppearingOnce(self, numbers):
        if not numbers or len(numbers) <= 3:
            return
        bitSum = [0] * 32
        for num in numbers:
            bitMask = 1
            for i in range(31, -1, -1):
                bit = num & bitMask
                if bit != 0:
                    bitSum[i] += 1
                bitMask = bitMask << 1

        result = 0
        for j in range(32):
            result = result << 1
            result += bitSum[j] % 3

        return result



# test 
s = Solution()
print(s.FindNumsAppearOnce([2, 4, 3, 6, 3, 2, 5, 5]))
print(s.FindNumberAppearingOnce([3, 1, 3, 3, 2, 2, 2]))