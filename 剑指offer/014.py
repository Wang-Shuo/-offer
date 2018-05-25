# -*- coding:utf-8 -*-
class Solution1:
    def maxProductAfterCutting(self, length):
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2

        products = [0] * (length + 1)
        products[0], products[1], products[2], products[3] = 0, 1, 2, 3

        maxProduct = 0
        for i in range(4, length + 1):
            maxProduct = 0
            for j in range(1, (i // 2) + 1):
                product = products[j] * products[i - j]
                if maxProduct < product:
                    maxProduct = product

                products[i] = maxProduct

        maxProduct = products[length]
        return maxProduct


class Solution2:
    def maxProductAfterCutting(self, length):
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2

        timesOf3 = length / 3
        if (length - timesOf3 * 3) == 1:
            timesOf3 -= 1

        timesOf2 = (length - timesOf3 * 3) / 2

        return (3 ** timesOf3) * (2 ** timesOf2)

# test
s = Solution2()
print(s.maxProductAfterCutting(8))
print(s.maxProductAfterCutting(0))
print(s.maxProductAfterCutting(1))
print(s.maxProductAfterCutting(2))
print(s.maxProductAfterCutting(3))
print(s.maxProductAfterCutting(4))
