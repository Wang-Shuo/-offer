# -*- coding:utf-8 -*-
class Solution:
    def Find(self, array, target):
        if array == []:
            return False

        num_rows = len(array)
        num_cols = len(array[0])

        i = 0
        j = num_cols - 1

        while i < num_rows and j >= 0:
            if array[i][j] > target:
                j -= 1
            elif array[i][j] < target:
                i += 1
            else:
                return True

        return False


# test case 
array1 = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]
array2 = []

s = Solution()
print(s.Find(array1, 7))
print(s.Find(array2, 7))
