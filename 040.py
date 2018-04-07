# -*- coding: utf-8 -*-
class Solution1:
    def Partition(self, numbers, length, start, end):
        if not numbers or length <= 0 or start < 0 or end >= length or start > end:
            return
        if end == start:
            return end
        pivot = numbers[start]
        left = start + 1
        right = end
        flag = False

        while not flag:
            while numbers[left] <= pivot and left <= right:
                left += 1
            while numbers[right] >= pivot and right >= left:
                right -= 1
            
            if left > right:
                flag = True
            else:
                numbers[left], numbers[right] = numbers[right], numbers[left]
        
        numbers[right], numbers[start] = numbers[start], numbers[right]

        return right

    def GetKLeastNumbers(self, array, k):
        if not array or len(array) <= 0 or len(array) < k or k <= 0:
            return
        
        n = len(array)
        start = 0
        end = n - 1
        index = self.Partition(array, n, start, end)
        while index != k - 1:
            if index > k - 1:
                end = index - 1
                index = self.Partition(array, n, start, end)
            else:
                start = index + 1
                index = self.Partition(array, n, start, end)
        output = array[:k]
        output.sort()
        return output


class Solution2:
    def GetKLeastNumbers(self, array, k):
        import heapq
        if not array or len(array) <= 0 or len(array) < k or k <= 0:
            return
        
        output = []
        for number in array:
            if len(output) < k:
                output.append(number)
            else:
                output = heapq.nlargest(k, output)
                if number >= output[0]:
                    continue
                else:
                    output[0] = number
        return output[::-1]


# test
array = [4, 5, 1, 6, 2 ,7, 3, 8]
s1 = Solution1()
s2 = Solution2()
print(s1.GetKLeastNumbers(array, 4))
print(s2.GetKLeastNumbers(array, 4))



