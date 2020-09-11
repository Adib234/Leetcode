class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            s = str(nums[i])
            if len(s) % 2 == 0:
                total += 1
        return total
