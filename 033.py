# -*- coding: utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, squence):
        if not squence or len(squence) == 0:
            return False

        root = squence[-1]
        length = len(squence)
        idx = 0
        for i in range(length - 1):
            idx = i
            if squence[i] > root:
                break

        for j in range(idx + 1, length - 1):
            if squence[j] < root:
                return False

        left = True
        if idx > 0:
            left = self.VerifySquenceOfBST(squence[:idx])

        right = True
        if idx < length - 1:
            right = self.VerifySquenceOfBST(squence[idx:length-1])

        return left and right


# test
array = [5, 7, 6, 9, 11, 10, 8]
array1 = [7, 4, 6, 5]
s = Solution()
print(s.VerifySquenceOfBST(array))
print(s.VerifySquenceOfBST(array1))

