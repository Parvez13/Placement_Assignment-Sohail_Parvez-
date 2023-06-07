def squareSorted(nums):
    result = []
    for i in range(len(nums)):
        result.append(nums[i]**2)
    result.sort()
    return result
# Tc: O(n)
# SC: O(1)
nums = [-9,-4, -1, 0, 3, 10]
print(squareSorted(nums))