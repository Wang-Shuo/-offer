# -*- coding: utf-8 -*-
class Solution:
    def Reverse(self, sList):
        if not sList or len(sList) <= 0:
            return ''
        startIdx = 0
        endIdx = len(sList) - 1
        while startIdx < endIdx:
            sList[startIdx], sList[endIdx] = sList[endIdx], sList[startIdx]
            startIdx += 1
            endIdx -= 1
        return sList

    def ReverseSentence(self, s):
        if not s or len(s) <= 0:
            return ''
        strList = list(s)
        strList = self.Reverse(strList)
        pBegin = 0
        pEnd = 0
        result = ''
        resultList = []
        while pEnd < len(s):
            if pEnd == len(s) - 1:
                resultList.append(self.Reverse(strList[pBegin:]))
                break
            if strList[pBegin] == ' ':
                pBegin += 1
                pEnd += 1
                resultList.append(' ')
            elif strList[pEnd] == ' ':
                resultList.append(self.Reverse(strList[pBegin:pEnd]))
                pBegin = pEnd
            else:
                pEnd += 1

        for c in resultList:
            result += ''.join(c)

        return result


    def ReverseSentence2(self, s):
        l = s.split(' ')
        return ' '.join(l[::-1])
# test
s = Solution()
print(s.ReverseSentence('I am a student.'))
print(s.ReverseSentence2('I am a student.'))
print(s.ReverseSentence(' I am a student. '))