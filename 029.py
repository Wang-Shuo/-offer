# -*- coding: utf-8 -*-
class Solution:
    def PrintMatrixClock(self, matrix):
        if not matrix or matrix == []:
            return

        output = []
        start = 0
        rows = len(matrix)
        cols = len(matrix[0])

        while cols > 2 * start and rows > start * 2:
            endX = cols - 1 - start
            endY = rows - 1 - start

            for i in range(start, endX + 1):
                num = matrix[start][i]
                output.append(num)

            if start < endY:
                for i in range(start + 1, endY + 1):
                    num = matrix[i][endX]
                    output.append(num)

            if start < endX and start < endY:
                for i in range(endX - 1, start - 1, -1):
                    num = matrix[endY][i]
                    output.append(num)

            if start < endX and start < (endY - 1):
                for i in range(endY - 1, start, -1):
                    num = matrix[i][start]
                    output.append(num)

            start += 1

        return output


# test
matrix = [[ 1,  2,  3,  4],
          [ 5,  6,  7,  8],
          [ 9, 10, 11, 12],
          [13, 14, 15, 16]]

s = Solution()
print(s.PrintMatrixClock(matrix))
