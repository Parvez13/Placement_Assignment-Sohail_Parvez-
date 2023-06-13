def isPowerOfThree(n):
	if n==1:
		return True
	if n==0:
		return False
	return isPowerOfThree(n/3)

n = 6
print(isPowerOfThree(n))