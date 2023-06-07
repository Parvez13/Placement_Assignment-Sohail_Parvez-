def findNTerm(a, d, N):
	if N==1:
		return a
	return findNTerm(a+d, d, N-1)

a=5
d=2
N=10
print(findNTerm(a, d, N))