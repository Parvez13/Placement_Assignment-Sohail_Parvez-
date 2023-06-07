def exponent(N, P):
	if N==0:
		return 0
	if P==0:
		return 1
	return N**P
# TC: O(1)
# SC: O(1)

N=2
P=0
print(exponent(N,P))