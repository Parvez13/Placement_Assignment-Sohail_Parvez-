def twodarray(nums, m, n):
	ans = []
	if len(nums) == m * n:
	    for r in range(m):
	        ans.append([])
	        # print(ans)
	        for c in range(n):
	            ans[-1].append(nums[r * n + c])
	return ans

nums = [1, 2, 3, 4, 5, 6]
m = 3
n = 2
print(twodarray(nums, m, n))