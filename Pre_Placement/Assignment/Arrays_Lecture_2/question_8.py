def solution(nums, k):
    if k == 0:
        return 0
    sol_array = []
    for i in range(len(nums)):
        for x in range(-k,k+1):
            temp_array = []
            temp_array.append(nums[i]+x)
            sol_array.extend(temp_array)
    return max(sol_array)-min(sol_array)
# TC: O(N^2)
# SC: O(N)
nums= [1]
k= 3
print(solution(nums, k))
