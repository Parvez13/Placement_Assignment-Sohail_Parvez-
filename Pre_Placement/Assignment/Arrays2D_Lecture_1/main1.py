# def isPresent(arr1, arr2, arr3):
#     result = []
#     temp_array = []
#     for i in range(len(arr1)):
#         if arr1[i] in arr2:
#             temp_array.append(arr1[i])
#     for j in range(len(temp_array)):
#         if temp_array[j] in arr3:
#             result.append(temp_array[j])
#     return result
# This approach  not good if there are any duplicate values
# # TC: O(N*N)-> O(N^2)-> O(N)
# # SC: O(N)

## Approach 2 : Using Hashset
def isPresent(arr1, arr2, arr3):
    hashset1 = set()
    hashset2 = set()
    hashset3 = set()

    for i in range(len(arr1)):
        hashset1.add(arr1[i])
    for j in range(len(arr2)):
        hashset2.add(arr2[j])
    
    for k in range(len(arr3)):
        if arr3[k] in hashset1 and arr3[k] in hashset2:
            if arr3[k] not in hashset3:
                hashset3.add(arr3[k])
    return hashset3
# TC: O(n+n+n)-> O(3n)-> O(n)
# SC: O(3n)-> O(n)
arr1 = [1, 2, 3, 4, 5, 5]
arr2 = [1, 2, 3,  5, 7, 9]
arr3 = [1, 3, 4, 5, 8]
print(isPresent(arr1, arr2, arr3))