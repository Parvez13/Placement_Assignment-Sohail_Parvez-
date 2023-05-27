# Return indices

def twoSum(nums, target):
    
    d = {}
    for i, j in enumerate(nums):
        r = target - j
        if r in d: 
            return [d[r], i]
        d[j] = i
		

if __name__ == '__main__':
    arr = [2,8, 15, 4, 7,11,15]
    k = 9
    sol = twoSum(arr, k)
    print(sol)