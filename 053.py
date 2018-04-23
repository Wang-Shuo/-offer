# -*- coding: utf-8 -*-
class Solution:
    def GetFirstK(self, data, length, k, start, end):
        if start > end:
            return -1

        middleIndex = (start + end) // 2
        middleData = data[middleIndex]

        if middleData == k:
            if (middleIndex > 0 and data[middleIndex - 1] != k) or middleIndex == 0:
                return middleIndex
            else:
                end = middleIndex - 1

        elif middleData > k:
            end = middleIndex - 1
        else:
            start = middleIndex + 1

        return self.GetFirstK(data, length, k, start, end)


    def GetLastK(self, data, length, k, start, end):
        if start > end:
            return -1
        
        middleIndex = (start + end) // 2
        middleData = data[middleIndex]

        if middleData == k:
            if (middleIndex < length - 1 and data[middleIndex + 1] != k) or middleIndex == (length - 1):
                return middleIndex
            else:
                start = middleIndex + 1

        elif middleData < k:
            start = middleIndex + 1
        else:
            end = middleIndex - 1

        return self.GetLastK(data, length, k, start, end)

    def GetNumberOfK(self, data, length, k):
        number = 0
        if data and length > 0:
           first = self.GetFirstK(data, length, k, 0, length - 1)
           last = self.GetLastK(data, length, k, 0, length - 1)

           if first > -1 and last > -1:
               number = last - first + 1

        return number


    def GetMissingNumber(self, numbers, length):
        if not numbers or length <= 0:
            return -1
        
        left = 0
        right = length - 1
        while left <= right:
            middle = (right + left) >> 1
            if numbers[middle] != middle:
                if middle == 0 or numbers[middle - 1] == middle - 1:
                    return middle
                right = middle - 1
            else:
                left = middle + 1

        if left == length:
            return length

        return -1



# test
s = Solution()
print(s.GetNumberOfK([1, 2, 3, 3, 3, 3, 4, 5], 8, 3)) 
print(s.GetMissingNumber([0, 1, 2, 4], 4))