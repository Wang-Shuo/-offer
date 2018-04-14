# -*- coding: utf-8 -*-
class Solution:
    def GetTranslationCount(self, number):
        if number < 0:
            return 0

        numStr = str(number)
        length = len(numStr)
        counts = [0] * length
        count = 0

        for i in range(length-1, -1, -1):
            count = 0
            if i < length - 1:
                count = counts[i + 1]
            else:
                count = 1

            if i < length - 1:
                digit1 = int(numStr[i])
                digit2 = int(numStr[i+1])
                converted = digit1 * 10 + digit2
                if converted >= 10 and converted <= 25:
                    if i < length - 2:
                        count += counts[i + 2]
                    else:
                        count += 1
            
            counts[i] = count

        count = counts[0]

        return count


# test
s = Solution()
print(s.GetTranslationCount(12258))
print(s.GetTranslationCount(-1))
print(s.GetTranslationCount(0))
print(s.GetTranslationCount(12345))