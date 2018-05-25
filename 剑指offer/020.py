# -*- coding: utf-8 -*-
class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s.strip()) == 0:
            return False

        strList = [w.lower() for w in s.strip()]
        if 'e' in strList:
            idxE = strList.index('e')
            left = strList[:idxE]
            right = strList[idxE+1:]

            if '.' in right or len(right) == 0 or len(left) == 0:
                return False

            isLeft = self.scanDigit(left)
            isRight = self.scanDigit(right)
            return isLeft and isRight
        else:
            isNum = self.scanDigit(strList)
            return isNum

    def scanDigit(self, strList):
        dotNum = 0
        digitNum = 0
        digitList = [str(i) for i in range(10)] + ['+', '-', '.']

        for i in range(len(strList)):
            if strList[i] not in digitList:
                return False
            if strList[i] == '.':
                dotNum += 1
            if strList[i] in [str(i) for i in range(10)]:
                digitNum += 1
            if strList[i] in ['+', '-'] and i != 0:
                return False

        if dotNum > 1:
            return False
        if digitNum == 0:
            return False
        return True

# test
s = Solution()
print(s.isNumber('+100'))
print(s.isNumber('5e2'))
print(s.isNumber('+123e-12'))
print(s.isNumber('.1'))
print(s.isNumber('12e'))
print(s.isNumber('1.2.3'))
print(s.isNumber('-+5'))
print(s.isNumber('12e+5.4'))
print(s.isNumber('+10e-'))
print(s.isNumber('-1E-16'))
print(s.isNumber('.e12'))
print(s.isNumber('3'))
