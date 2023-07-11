class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # Maximum element in the array
        place = arr.index(max(arr)) 
        # if only one element is left
        # or less than 3 elements
        if place == 0 or place == len(arr)-1:
            return False
        else:
            value = True
            i = 0
            # more than one elements
            while i < place:
                # Index '0' must be less than the index '1'
                if arr[i] >= arr[i+1]:
                    value = False:
                    break
                else:
                    i += 1
            i = place + 1
            if value:
                while i < len(arr):
                    if arr[i-1] <= arr[i]:
                        # print(i)
                        return False
                    else:
                        i += 1
            else:
                return False
            return True