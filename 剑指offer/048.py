# -*- coding: utf-8 -*-
class Solution:
    def LongestSubstrWithoutDuplication(self, string):
        curLength = 0
        maxLength = 0

        position = [-1] * 26
        for i in range(len(string)):
            pidx = ord(string[i]) - ord('a')
            prevIndex = position[pidx]
            if prevIndex < 0 or i - prevIndex > curLength:
                curLength += 1
            else:
                if curLength > maxLength:
                    maxLength = curLength

                curLength = i - prevIndex

            position[pidx] = i

        if curLength > maxLength:
            maxLength = curLength

        return maxLength


# test 
s = Solution()
print(s.LongestSubstrWithoutDuplication('arabcacfr'))