def findMissingElement(nums):
	nums.sort()
	start = 0
	end = len(nums)-1
	while(start<=end):
		mid = (start+end)//2
		if nums[mid] == mid:
			start = mid+1
		else:
			end = mid -1 
	return start 

nums = [9,6,4,2,3,5,7,0,1,8, 11]
print(findMissingElement(nums))