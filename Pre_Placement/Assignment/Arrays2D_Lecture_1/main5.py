import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1+ math.sqrt(1+8*n))//2)

# TC: O(1)
# SC: O(1)
sol = Solution()
print(sol.arrangeCoins(n=11))