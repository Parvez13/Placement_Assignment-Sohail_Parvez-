def findMaximum(arr,n):
	if n == 0:
		return -1
	if n==1:
		return arr[0]
	return max(arr[n-1], findMaximum(arr,n-1))
# TC: O(n)
# SC: O(n)
arr = [1, 4, 3, -5, -4, 8, 6]
n= len(arr)
print(findMaximum(arr, n))