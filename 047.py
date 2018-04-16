# -*- coding: utf-8 -*-
class Solution:
    def GetMaxValue(self, values, rows, cols):
        if not values or rows < 0 or cols < 0:
            return 0
        
        maxValues = [0] * cols
        for i in range(rows):
            for j in range(cols):
                left = 0
                up = 0
                if i > 0:
                    up = maxValues[j]
                if j > 0:
                    left = maxValues[j - 1]
                maxValues[j] = max(left, up) + values[i * cols + j]

        maxValue = maxValues[cols - 1]

        return maxValue


# test 
s = Solution()
print(s.GetMaxValue([1, 10, 3, 8, 12, 2, 9, 6, 5, 7, 4, 11, 3, 7, 16, 5], 4, 4))