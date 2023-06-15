def merge_arrays(nums1, nums2, m, n):
    # Two pointer approach
    i = m - 1
    j = n - 1
    k = m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

nums1 = [1, 2, 3, 0,0,0]
nums2 = [2, 5, 6,1]
m = 3
n = 3
sol = merge_arrays(nums1, nums2, m, n)
print(sol)

