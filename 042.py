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

# test
s = Solution()
print(s.FindGreatestSumOfSubArray([1, -2, 3, 10, -4, 7, 2, -5]))
print(s.FindGreatestSumOfSubArray([1, 2, -3, 4, 5]))
print(s.FindGreatestSumOfSubArray([]))