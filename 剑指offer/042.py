# -*- coding: utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, numbers):

        if len(numbers) <= 0 or not numbers:
            return

        curSum = 0
        maxSum = numbers[0]
        for num in numbers:
            if curSum <= 0:
                curSum = num
            else:
                curSum += num

            if curSum > maxSum:
                maxSum = curSum

        return maxSum

class Solution2:
    def FindGreatestSumOfSubArray(self, numbers):
        if len(numbers) <= 0 or not numbers:
            return

        sumList = [0] * len(numbers)
        for i in range(len(numbers)):
            if i == 0 or sumList[i-1] <= 0:
                sumList[i] = numbers[i]
            else:
                sumList[i] = sumList[i-1] + numbers[i]
        
        return max(sumList)

# test
s = Solution2()
print(s.FindGreatestSumOfSubArray([1, -2, 3, 10, -4, 7, 2, -5]))
print(s.FindGreatestSumOfSubArray([1, 2, -3, 4, 5]))
print(s.FindGreatestSumOfSubArray([]))