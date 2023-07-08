# Alice has n no of different types of candies
def get_candies(candies):
    if len(candies)%2 != 0:
        return 0
    unique_candies = 0
    for i in range(len(candies)):
        for j in range(0,i):
            if candies[i] == candies[j]:
                break 
        else:
            unique_candies += 1
    return max(unique_candies, len(candies)//2)
#TC: O(N^N)-> O(N^2)
#SC: O(1)
candies = [1,1,2,2,3,8,4,4,5,6,6,6,8,10,7,9]
sol = get_candies(candies)
print(sol)