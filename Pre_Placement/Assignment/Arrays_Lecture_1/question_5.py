def merge_arrays(nums1, nums2, m, n):
    nums1 = list(filter(lambda x : x != 0, nums1))
    nums2 = list(filter(lambda y: y !=0, nums2))
    nums = nums1[:m] + nums2[:n]
    return sorted(nums)

nums1 = [1, 2, 3, 0,0,0]
nums2 = [2, 5, 6,1]
m = 3
n = 3
sol = merge_arrays(nums1, nums2, m, n)
print(sol)

