def searchMatrix(matrix, target):
	# Binary search
	row, col = len(matrix), len(matrix[0])
	i, j = 0, (row*col)-1
	while i <= j:
		mid = (i+j) >> 1
		mid_element = matrix[mid//col][mid%col]
		if mid_element == target:
			return True
		elif mid_element < target:
			i = mid + 1
		else:
			j = mid - 1
	return False
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 5
print(searchMatrix(matrix, target))
