def ending_zeros(nums):
    n = len(nums)
    for i in range(0,n):
        if nums[i] == 0:
            nums.remove(nums[i])
            nums.append(0)
    return nums
        



nums = [1, 0, 1, 3, 2, 0, 0, 5]
sol = ending_zeros(nums)
print(sol)
