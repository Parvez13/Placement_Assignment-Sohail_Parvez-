def findClosest(nums, target):
    n = len(nums)
    left_pointer = 0
    right_pointer = n-1
    while left_pointer < right_pointer:  # loop till 0<8[n-1](n=9)
        if abs(nums[left_pointer] - target) <= abs(nums[right_pointer]-target):
            right_pointer -= 1
        else:
            left_pointer += 1
            
    return nums[left_pointer]
# TC: O(N)
# SC: O(1)
nums = [1, 2, 4, 5, 6, 6, 8, 9]
target = 11
# print(len(nums))
print(findClosest(nums, target))