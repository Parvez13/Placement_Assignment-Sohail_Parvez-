def max_possible_sum(array):
    array.sort()  # Sort the array in ascending order
    max_sum = 0 # Assign max_sum equals to zero

    for i in range(0, len(array),2): # Loop through length of array with step 2 so that ith value is even 
        pair_sum = min(array[i], array[i+1])  # Calculate the min value of array[i], array[i+1](thats why we are range with step 2, so that the array[i] is step2(0,2,4..) and array[i+1] = 0+1(1),2+1=3)
        max_sum += pair_sum
       # print(f'i: {i}, array: {array},array[i]:{array[i]}, array[i+1]: {array[i+1]}, pairsum: {pair_sum},max_sum: {max_sum}')       
    return max_sum
# TC: O(Nlogn)
# SC: O(N)
array = [0,2, 5, 3,1, 2]
sol = max_possible_sum(array)
print(sol)
