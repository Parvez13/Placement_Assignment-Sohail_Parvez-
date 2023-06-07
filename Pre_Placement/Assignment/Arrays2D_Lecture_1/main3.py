# Transpose of matrix
def transpose_matrix(matrix):
    row = len(matrix)
    col = len(matrix[0])
    ans = [[0 for _ in range(row)] for _ in range(col)] # Create dummy array with all elements having 0's

    for r in range(row):
        for c in range(col):
            ans[r][c] = matrix[c][r]
    return ans
# TC: O(mxn)
# SC: O(1)
matrix = [[1,2,3],[4, 5, 6],[7,8,9]]
print(transpose_matrix(matrix))