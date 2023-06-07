def productOfArray(arr):
	n = len(arr)
	if n == 0:
		return 1
	if n==1:
		return arr[0]
	return arr[0]*productOfArray(arr[1:])
# TC: O(n)
# SC: O(n)
arr = [1,6,3]
print(productOfArray(arr))