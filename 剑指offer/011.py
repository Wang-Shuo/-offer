# -*- coding:utf-8 -*-
class Solution:
    def minInRotate(self, numbers):
        if len(numbers) <= 0:
            return

        idx1 = 0
        idx2 = len(numbers) - 1
        idxMid = idx1

        while numbers[idx1] >= numbers[idx2]:
            if idx2 - idx1 == 1:
                idxMid = idx2
                break

            idxMid = (idx1 + idx2) / 2

            if numbers[idx1] == numbers[idx2] and numbers[idxMid] == numbers[idx1]:
                return self.minInOrder(numbers, idx1, idx2)

            if numbers[idxMid] >= numbers[idx1]:
                idx1 = idxMid
            elif numbers[idxMid] <= numbers[idx2]:
                idx2 = idxMid

        return numbers[idxMid]


    def minInOrder(self, numbers, idx1, idx2):
        minium = numbers[idx1]
        for i in range(idx1 + 1, idx2 + 1):
             if minium > numbers[i]:
                 minium = numbers[i]

        return minium


# test
s = Solution()
nb1 = [3,3,5,2,2]
nb2 = [2,2,3,3,4]
nb3 = [1,1,2,1,1]

print(s.minInRotate(nb1))
print(s.minInRotate(nb2))
print(s.minInRotate(nb3))
