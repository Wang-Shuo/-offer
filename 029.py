# -*- coding: utf-8 -*-
class Solution:
    def PrintMatrixClock(self, matrix):
        if not matrix or matrix == []:
            return

        start = 0
        rows = len(matrix)
        cols = len(matrix[0])

        while cols > 2 * start and rows > start * 2:
            endX = cols - 1 - start
            endY = rows - 1 - start



