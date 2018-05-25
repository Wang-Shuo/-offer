# -*- coding: utf-8 -*-
class Solution:
    def maxInWindows(self, numbers, size):
        if not numbers or size <= 0:
            return []
        deque = []
        if len(numbers) >= size:
            index = []
            for i in range(size):
                while len(index) > 0 and numbers[i] >= numbers[index[-1]]:
                    index.pop()
                index.append(i)

            for i in range(size, len(numbers)):
                deque.append(numbers[index[0]])
                while len(index) > 0 and numbers[i] >= numbers[index[-1]]:
                    index.pop()
                if len(index) > 0 and index[0] <= i - size:
                    index.pop(0)
                index.append(i)

            deque.append(numbers[index[0]])
        return deque


# test
s = Solution()
print(s.maxInWindows([2, 3, 4, 2, 6, 2, 5, 1], 3))