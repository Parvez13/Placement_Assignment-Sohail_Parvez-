class Solution:
    def diStringMatch(self, s: str):
        i, n = 0, len(s)
        ans = []
        for c in s:
            if c == 'I': 
                ans.append(i)
                i+=1
            else:
                ans.append(n)
                n-=1
        ans.append(i)
        return ans

s = "SOHAIL"
sol = Solution()
print(sol.diStringMatch(s))