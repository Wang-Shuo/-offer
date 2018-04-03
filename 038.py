# -*- coding: utf-8 -*-
class Solution:
    def Permutation(self, s):
        if not len(s):
            return []
        if len(s) == 1:
            return list(s)

        result = []
        for i in range(len(s)):
            ss = s[:i] + s[i+1:]
            p = self.Permutation(ss)
            for pp in p:
                result.append(s[i] + pp)
        return result


    def Combination(self, s):
        if not len(s):
            return []
        if len(s) == 1:
            return list(s)
        
        charList = list(s)
        charList.sort()
        result = []
        for i in range(len(charList)):
            result.append(charList[i])
            if i > 0 and charList[i] == charList[i - 1]:
                continue
            temp = self.Combination(''.join(charList[i + 1:]))
            for j in temp:
                result.append(charList[i] + j)
            result = list(set(result))
            result.sort()
        return result
            
# test
s = Solution()
print(s.Permutation('abc'))
print(s.Combination('abc'))