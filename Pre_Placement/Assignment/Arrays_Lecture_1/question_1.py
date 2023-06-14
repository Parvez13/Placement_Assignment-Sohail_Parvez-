# Return indices

def twoSum(nums, target):
   hashmap = {}
   for index, current_element in enumerate(nums):
	   if target - current_element in hashmap.keys():
		   return [hashmap[current_element], index]
	   else:
		   hashmap[current_element] = index
		

if __name__ == '__main__':
    arr = [2,8, 15, 4, 7,11,15]
    k = 9
    sol = twoSum(arr, k)
    print(sol)
