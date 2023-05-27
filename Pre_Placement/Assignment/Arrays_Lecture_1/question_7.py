def ending_zeros(nums):
    n = len(nums)
    j = 0
    for i in range(n):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    return nums
        



nums = [1, 0, 1, 3, 2, 0, 0, 5]
sol = ending_zeros(nums)
print(sol)