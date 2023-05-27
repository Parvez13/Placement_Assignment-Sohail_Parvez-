# Remove the val in nums
def remove_val(nums, val):
    res = [i for i in nums if i != val]
    return len(res), res[:2]

if __name__ == '__main__':
    nums = [3, 2, 2, 3, 6, 7, 8]
    val = 3
    sol = remove_val(nums, val)
    print(sol)