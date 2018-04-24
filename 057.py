# -*- coding: utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, numbers, twoSum):
        if len(numbers) < 1 or not numbers:
            return
        ahead = len(numbers) - 1
        behind = 0

        while ahead > behind:
            curSum = numbers[ahead] + numbers[behind]
            if curSum == twoSum:
                return [numbers[behind], numbers[ahead]]
                break
            elif curSum > twoSum:
                ahead -= 1
            else:
                behind += 1


    def FindContinuousSequence(self, sum):
        if sum < 3:
            return
        small = 1
        big = 2
        result = []
        middle = (1 + sum) / 2
        curSum = small + big
        while small < middle:
            if curSum == sum:
                result.append([i for i in range(small, big + 1)])

            while curSum > sum and small < middle:
                curSum -= small
                small += 1
            
                if curSum == sum:
                    result.append([i for i in range(small, big + 1)])

            big += 1
            curSum += big

        return result


# test
s = Solution()
print(s.FindNumbersWithSum([1, 2, 4, 7, 11, 15], 15))
print(s.FindNumbersWithSum([1, 2, 4, 7], 10))
print(s.FindContinuousSequence(15))