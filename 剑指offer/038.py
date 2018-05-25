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

    def CubicSum(self, num_array):
        num_array = [str(num) for num in num_array]
        num_str = ''.join(num_array)
        totalPerms = self.Permutation(num_str)
        for perm in totalPerms:
            sum1 = int(perm[0]) + int(perm[1]) + int(perm[2]) + int(perm[3])
            sum2 = int(perm[4]) + int(perm[5]) + int(perm[6]) + int(perm[7])
            sum3 = int(perm[0]) + int(perm[2]) + int(perm[4]) + int(perm[6])
            sum4 = int(perm[1]) + int(perm[3]) + int(perm[5]) + int(perm[7])
            sum5 = int(perm[0]) + int(perm[1]) + int(perm[4]) + int(perm[5])
            sum6 = int(perm[2]) + int(perm[3]) + int(perm[6]) + int(perm[7])
            if sum1 == sum2 and sum3 == sum4 and sum5 == sum6:
                return True
        return False


    def Queen(self, num_array):
        num_array = [str(num) for num in num_array]
        num_str = ''.join(num_array)
        totalPerms = self.Permutation(num_str)
        def Judge(posList):
            length = len(posList)
            for i in range(length):
                for j in range(length):
                    if i == j:
                        continue
                    if i - j == int(posList[i]) - int(posList[j]) or j - i == int(posList[i]) - int(posList[j]):
                        return False
            return True
        
        for posList in totalPerms:
            isQueen = Judge(posList)
            if isQueen:
                print(posList)

            
# test
s = Solution()
print(s.Permutation('abc'))
print(s.Combination('abc'))
print(s.CubicSum([1, 1, 1, 1, 1, 1, 1, 1]))
s.Queen([0, 1, 2, 3, 4, 5, 6, 7])