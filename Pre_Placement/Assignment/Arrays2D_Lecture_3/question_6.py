# def return_original(arr):
# 	for i in range(len(arr)):
# 		if arr[i]*2  in arr:
# 			return arr[:(arr[i]*2)+1]
# 		else:
# 			return -1
from collections import Counter
class Solution:
    def findOriginalArray(self, changed):
        if len(changed) % 2 == 1:
            return []
        data = Counter(changed)
        result = []
        for k in sorted(data):
            if data[k] < 0:
                return []
            value = k * 2
            while data[k] > 0:
                if data[value] == 0:
                    return []
                result.append(k)
                data[k] -= 1
                data[value] -= 1
        return result

arr = [1, 3, 4, 5, 6, 2, 6, 8, 10, 12]
sol = Solution()
print(sol.findOriginalArray(arr))