def find_index(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i 
        elif nums[i] > target:
            return i
    return len(nums)

if __name__ == '__main__':
    nums = [1, 2,5,6]
    target = 5
    sol = find_index(nums, target)
    print(sol)
    # if the value is not in index
    target = 7
    sol2 = find_index(nums, target)
    print(sol2)