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


# test
s = Solution()
print(s.FindNumbersWithSum([1, 2, 4, 7, 11, 15], 15))
