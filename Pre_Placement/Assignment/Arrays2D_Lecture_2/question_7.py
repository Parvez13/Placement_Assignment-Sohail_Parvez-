def ismonotonic(nums):
    for i in range(len(nums)):
        for j in range(1,len(nums)): # i<j
            # print(i,j)
            if nums[i] < nums[j] or nums[i] > nums[j]: # increasing elements or decreasing
                return True 
    return False
# TC: O(N^2)
# SC: O(1)
nums = [0,3,5, -1] # increasing or decreasing -> True
nums= [1,1, 1, 1] # neither increasing nor decreasing -> False
print(ismonotonic(nums))