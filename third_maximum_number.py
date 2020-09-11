class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        distinct = 0
        if len(nums) >= 3:
            for i in range(len(nums)-1, 0, -1):
                if nums[i] != nums[i-1]:
                    distinct += 1
                if distinct == 2:
                    third = nums[i-1]
                    break
        return max(nums) if distinct != 2 or len(nums) < 3 else third
