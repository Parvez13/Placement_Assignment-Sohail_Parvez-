from collections import deque
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B:
            return True

        q1, q2 = deque(), deque()

        for i in A:
            q1.append(i)

        for i in B:
            q2.append(i)

        """
        We can condense above steps as 
        q1, q2 = deque(A), deque(B)
        """

        i = 0
        while i < len(A):
            q1.append(q1.popleft())
            if q1 == q2:
                return True
            i += 1

        return False
s = "abcdefgh"
goal = "cdefghab"
sol = Solution()
print(sol.rotateString(s, goal))