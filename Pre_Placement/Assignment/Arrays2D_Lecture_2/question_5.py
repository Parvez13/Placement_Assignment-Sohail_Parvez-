import sys
 
def maxProduct(arr, n):
 
    # If size is less than 3,return -1
    if (n < 3):
        return -1
 
    # Initialize Maximum, second
    # maximum and third maximum
    # element
    maxA = -sys.maxsize - 1
    maxB = -sys.maxsize - 1
    maxC = -sys.maxsize - 1
 
    # Initialize Minimum and
    # second minimum element
    minA = sys.maxsize
    minB = sys.maxsize
 
    for i in range(n):
 
        # Update Maximum, second
        # maximum and third maximum
        # element
        if (arr[i] > maxA):
            maxC = maxB
            maxB = maxA
            maxA = arr[i]
             
        # Update second maximum and
        # third maximum element
        elif (arr[i] > maxB):
            maxC = maxB
            maxB = arr[i]
             
        # Update third maximum element
        elif (arr[i] > maxC):
            maxC = arr[i]
 
        # Update Minimum and second
        # minimum element
        if (arr[i] < minA):
            minB = minA
            minA = arr[i]
 
        # Update second minimum element
        elif (arr[i] < minB):
            minB = arr[i]
 
    return max(minA * minB,
               maxA * maxB * maxC)
 

arr = [ 1, 2, 3, 4, 7, 8]
n = len(arr)
# TC: O(N)
# SC: O(1)
Max = maxProduct(arr, n)
print(Max)


