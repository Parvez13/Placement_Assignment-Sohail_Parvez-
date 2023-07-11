def minValue(A, B):
	n = len(A)
	A.sort()
	B.sort()
	print(A)
	print(B)
	result = 0
	for i in range(n):
		result += (A[i] * B[n-i-1])
	return result

A = [5, 3, 4, 2]
B = [4, 2, 2, 5]
print(minValue(A, B))