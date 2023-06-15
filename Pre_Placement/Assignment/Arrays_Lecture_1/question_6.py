# find the number is present twice
def is_duplicate(nums):
    hash_set = set()
    for element in nums:
        if element in hashset:
            return True
        else:
            hashset.add(element)
    return False
    
nums = [1, 2, 3,1]
sol = is_duplicate(nums)
print(sol)
