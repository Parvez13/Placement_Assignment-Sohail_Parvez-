class Solution:
	def maxCount(self, m, n, ops):
		for r,c in ops:
			print(m,r)
			print()
			print(c,n)
			m = min(m,r)
			n = min(c,n)
		return m*n 
m = 3
n = 3 
ops=[[2,2],[3,3]]
sol = Solution()
print(sol.maxCount(m,n,ops))
