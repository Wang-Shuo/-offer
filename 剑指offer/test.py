# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if not s or len(s.strip()) == 0:
            return False
        
        strList = [w.lower() for w in s.strip()]
        if 'e' in strList:
            idxE = strList.index('e')
            left = strList[:idxE]
            right = strList[idxE+1:]
            if '.' in right:
                return False
            
            isLeft = self.scanDigit(left)
            isRight = self.scanDigit(right)
            return isLeft and isRight 
        else:
            return self.scanDigit(strList)
        
    def scanDigit(self, strList):
        dotNum = 0
        digitNum = 0
        digitList = [str(i) for i in range(10)] + ['+', '-', '.']
        
        for i, c in enumerate(strList):
            if c not in digitList:
                return False
            
            if c == '.':
                dotNum += 1
            
            if c in [str(j) for j in range(10)]:
                digitNum += 1
            
            if c in ['+', '-'] and i != 0:
                return False
            
        if dotNum > 1:
            return False
        if digitNum == 0:
            return False
        return True
               
s = Solution()
n = int(raw_input())
for i in range(n):
    line = raw_input()
    if s.isNumeric(line):
        print "TRUE"
    else:
        print "FALSE"