def minimum_element(arr):
	if len(arr)==1:
		return arr[0]

	left = 0
	right = len(arr)-1

	if arr[right] > arr[0]:
		return arr[0]

	while left <= right:
		mid = (left+right)//2
		if arr[mid] > arr[mid+1]:
			return arr[mid+1]
		if arr[mid-1] > arr[mid]:
			return arr[mid]
		if arr[mid]>arr[0]:
			left = mid+1
		else:
			right = mid-1

arr = [11,13,15,17]
print(minimum_element(arr))