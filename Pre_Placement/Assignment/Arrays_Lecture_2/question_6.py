# def ispresent(nums, target):
#     for i in range(len(nums)):
#         if nums[i] == target:
#             return i
#     return -1
# TC: O(N), SC: O(1)

# Searching algorithm whose time complexity is O(logN) is BinarySearch
def binarySearch(nums, target):
    left_side = 0
    right_side = len(nums)-1
    while left_side <= right_side:
        mid_value = (left_side + right_side) // 2
        if nums[mid_value] == target:
            return mid_value 
        elif nums[mid_value] < target:
            left_side = mid_value + 1 # target is smaller than mid value must be left side 
        else:
            right_side = mid_value - 1
    return -1


nums = [-1,0,3,5,9,12]
target = 12
print(binarySearch(nums, target))