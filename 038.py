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

# test
s = Solution()
print(s.Permutation('abc'))