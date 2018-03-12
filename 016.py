# -*- coding: utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        epsilon = 1e-7
        if base >= -epsilon and base <= epsilon and exponent < 0:
            return 0

        absExp = abs(exponent)
        result = 1.0
        for i in range(absExp):
            result = base * result

        if exponent < 0:
            result = 1.0 / result
        return result


class Solution2:
    def Power(self, base, exponent):
        epsilon = 1e-7
        if base >= -epsilon and base <= epsilon and exponent < 0:
            return 0
        if exponent == 0:
            return 1
        if exponent == 1:
            return base

        absExp = abs(exponent)
        result = self.Power(base, absExp >> 1)
        result *= result
        if (exponent & 0x1) == 1:
            result *= base

        if exponent < 0:
            result = 1.0 / result
        return result


# test
s = Solution2()
print(s.Power(2.0, 5))
print(s.Power(0.0, 5))
print(s.Power(2.0, 1))
print(s.Power(-2.0, 5))
print(s.Power(2.0, -5))
print(s.Power(2.0, 0))
print(s.Power(-2.0, 0))
