# -*- coding:utf-8 -*-
class Solution:
	def hasPath(self, matrix, rows, cols, str_path):
		if matrix is None or rows < 1 or cols < 1 or str_path is None:
			return False

		visited = [0] * (rows * cols)

		pathLength = 0
		for row in range(rows):
			for col in range(cols):
				if self.hasPathCore(matrix, rows, cols, row, col, str_path, pathLength, visited):
					return True

		return False


	def hasPathCore(self, matrix, rows, cols, row, col, str_path, pathLength, visited):
		if len(str_path) == pathLength:
			return True

		hasPath = False
		if row >= 0 and row < rows and col >= 0 and col < cols and \
		   matrix[row * cols + col] == str_path[pathLength] and \
		   not visited[row * cols + col]:

		    pathLength += 1
		    visited[row * cols + col] = 1

		    hasPath = self.hasPathCore(matrix, rows, cols, row, col-1, str_path, pathLength, visited) or \
		   			  self.hasPathCore(matrix, rows, cols, row-1, col, str_path, pathLength, visited) or \
		   			  self.hasPathCore(matrix, rows, cols, row, col+1, str_path, pathLength, visited) or \
		   			  self.hasPathCore(matrix, rows, cols, row+1, col, str_path, pathLength, visited)

		    if not hasPath:
		    	pathLength -= 1
		    	visited[row * cols + col] = 0

		return hasPath



# test
s = Solution()
result1 = s.hasPath('abtgcfcsjdeh', 3, 4, 'bfce')
result2 = s.hasPath('abtgcfcsjdeh', 3, 4, 'bcdh')
result3 = s.hasPath('abtg', 1, 4, 'abtg')
print(result1)
print(result2)
print(result3)
