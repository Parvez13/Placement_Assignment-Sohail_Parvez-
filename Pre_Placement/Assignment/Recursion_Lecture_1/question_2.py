def sumOfNums(n):
	if n<=0 or n==1:
		return n
	return n+sumOfNums(n-1)
# TC: O(n)
# SC: O(n)

n = 10
print(sumOfNums(n))