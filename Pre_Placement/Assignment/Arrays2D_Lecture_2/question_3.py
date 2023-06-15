def squareSorted(nums):
	result = []
	left_pointer = 0
	right_pointer = len(nums)-1
	while left_pointer <= right_pointer:
		if nums[left_pointer] * nums[left_pointer] > nums[right_pointer] * nums[right_pointer]:
			result.append(nums[left_pointer] * nums[left_pointer])
			left_pointer += 1
		else:
			result.append(nums[right_pointer] * nums[right_pointer])
			right_pointer -= 1
	return result[::-1]

nums = [-4, -1, 0, 3, 10]
print(squareSorted(nums))