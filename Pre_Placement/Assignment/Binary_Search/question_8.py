def repeating_element(nums1, nums2):
	set1 = nums1
	set2 = nums2
	answer = []
	for i in set1:
		if i in set2:
			answer.append(i)
	return answer 
# TC: O(logn)
# SC: O(1)
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(repeating_element(nums1, nums2))
