def find_index(nums, target):
    # for i in range(len(nums)):
    #     if nums[i] == target:
    #         return i 
    #     elif nums[i] > target:
    #         return i
    # return len(nums)
    start = 0
    end = len(nums)-1
    while(start<=end):
        mid = (start+end)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1

if __name__ == '__main__':
    nums = [1, 2,5,6]
    target = 5
    sol = find_index(nums, target)
    print(sol)
    # if the value is not in index
    target = 7
    sol2 = find_index(nums, target)
    print(sol2)
