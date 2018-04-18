# -*- coding: utf-8 -*-
class Solution:
    def InversePairs(self, data):
        length = len(data)
        if not data or length <= 0:
            return 0
        
        copy = [0] * length
        for i in range(length):
            copy[i] = data[i]
        
        count = self.InversePairsCore(data, copy, 0, length - 1)
        return count

    def InversePairsCore(self, data, copy, start, end):
        if start == end:
            copy[start] = data[start]
            return 0
        length = (end - start) // 2
        
        left = self.InversePairsCore(copy, data, start, start + length)
        right = self.InversePairsCore(copy, data, start + length + 1, end)

        i = start + length
        j = end
        indexCopy = end
        count = 0
        while i >= start and j >= start + length + 1:
            if data[i] > data[j]:
                copy[indexCopy] = data[i]
                indexCopy -= 1
                i -= 1
                count += j - start - length
            else:
                copy[indexCopy] = data[j]
                indexCopy -= 1
                j -= 1

        while i >= start:
            copy[indexCopy] = data[i]
            indexCopy -= 1
            i -= 1

        while j >= start + length + 1:
            copy[indexCopy] = data[j]
            indexCopy -= 1
            j -= 1

        return left + right + count


# test 
s = Solution()
print(s.InversePairs([7, 5, 6, 4]))

