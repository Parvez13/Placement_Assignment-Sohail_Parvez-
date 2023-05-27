# find the number is present twice
def is_duplicate(nums):
    hash_dict = {}
    for i in nums:
        if i  not in hash_dict:
            hash_dict[i] = 1
        else:
            return True 
    return False
nums = [1, 2, 3,1]
sol = is_duplicate(nums)
print(sol)