# -*- coding: utf-8 -*-
class Solution:
    def ReorderOddEven(self, array):
        if len(array) == 0 or not array:
            return

        left = 0
        right = len(array) - 1
        while left < right:
            while (left < right) and (array[left] & 0x1 == 1):
                left += 1
            while (left < right) and (array[right] & 0x1 == 0):
                right -= 1

            if left < right:
                array[right], array[left] = array[left], array[right]

        return array


# test
s = Solution()
print(s.ReorderOddEven([2,3,4,5,7]))
print(s.ReorderOddEven([1,3,3,5,7]))
print(s.ReorderOddEven([2,4,4,6,8]))
