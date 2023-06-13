def returnFinalElement(arr):

	if len(arr)==1:
		return arr[0]
	print("Original arr")
	print(arr)
	# Remove every element from left to right
	arr = arr[1::2]
	print("Left to right")
	print(arr)
	
	# reverse the list
	arr = arr[::-1]
	print("Right to left")
	print(arr)
	return returnFinalElement(arr)

n = 25
arr = list(range(1,n+1))
print(returnFinalElement(arr))
