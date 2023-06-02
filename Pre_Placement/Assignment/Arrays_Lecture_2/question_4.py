def isFlowerbedEmpty(flowerbed, n):
    f = [0] + flowerbed + [0] # Assume first and last element is having space
    # The flower can't be plotted adjacent of the other flower
    # So we have to check whether the position we are going to plot having empty(0) space before and after including target position
    for i in range(1, len(f)-1): 
        if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
            f[i] = 1
            n-=1
    return n<=0
# TC: O(N)
# SC: O(1)
flowerbed = [1,0,0,0,0,0,1]
n = 2
print(isFlowerbedEmpty(flowerbed, n))