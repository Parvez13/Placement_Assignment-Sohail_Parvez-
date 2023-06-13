class Solution:
    def __init__(self):
        self.s = 0
        self.ansA = -1

    def firstOcr(self, nums, target):
        e = len(nums) - 1

        while self.s <= e:
            mid = self.s + (e - self.s) // 2

            if nums[mid] == target:
                self.ansA = mid
                e = mid - 1
            elif nums[mid] > target:
                e = mid - 1
            else:
                self.s = mid + 1

        return self.ansA

    def LastOcr(self, nums, target):
        e = len(nums) - 1

        while self.s <= e:
            mid = self.s + (e - self.s) // 2

            if nums[mid] == target:
                self.ansA = mid
                self.s = mid + 1
            elif nums[mid] > target:
                e = mid - 1
            else:
                self.s = mid + 1

        return self.ansA

    def searchRange(self, nums, target):
        v = [-1,-1]
        v[0] = self.firstOcr(nums, target)
        v[1] = self.LastOcr(nums, target)

        return v
nums = [5, 7, 7, 8, 8, 10]
target =7
sol = Solution()
print(sol.searchRange(nums, target))

