def possible_pairsum(nums):
    nums.sort()
    print(nums)
    max_sum = 0
    for i in range(0, len(nums),2):
        pair_sum = min(nums[i], nums[i+1])
        max_sum += pair_sum
    return max_sum
# TC: O(n)
# SC: O(1)
nums = [1,4,3,2]
print(possible_pairsum(nums))