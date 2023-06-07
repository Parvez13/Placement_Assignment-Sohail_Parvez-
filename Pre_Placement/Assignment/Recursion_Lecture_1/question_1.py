def isPowerOfTwo(n):
	if n==1:
		return True 
	elif n%2 != 0 or n== 0:
		return False  
	return isPowerOfTwo(n/2) # Dividing until we get 1


n = 64
print(isPowerOfTwo(n))

