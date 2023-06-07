def returnDistinct(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    result  = [[],[]]
    for i in set1:
        if i not in set2:
            result[0].append(i)
    for  j in set2:
        if j not in set1:
            result[1].append(j)
    return result
# TC: O(2n)-> O(n)
# SC: O(1)
nums1 = [1, 2, 2, 3, 3]
nums2 = [1, 1, 2, 2]
print(returnDistinct(nums1, nums2))